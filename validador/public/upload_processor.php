<?php
// upload_processor.php

// Inclui as bibliotecas de terceiros necessárias para a geração de PDF e QR Code.
// Certifique-se de que os caminhos para essas bibliotecas estão corretos.
require_once(__DIR__. '/../private/lib/tcpdf/tcpdf.php');
require_once(__DIR__. '/../private/lib/phpqrcode/qrlib.php');

// --- CONFIGURAÇÕES ---
// Define o diretório de upload seguro, fora da raiz pública da web.
define('UPLOAD_DIR', __DIR__. '/../private/assinaturas/');
// Define o diretório temporário para os manifestos gerados.
define('MANIFEST_DIR', __DIR__. '/../private/manifestos/');
// Define o diretório temporário para as imagens de QR Code.
define('QR_TEMP_DIR', __DIR__. '/../private/qr_temp/');
// Define o tamanho máximo do arquivo em bytes (ex: 10 MB).
define('MAX_FILE_SIZE', 10 * 1024 * 1024);
// Define a URL base para o link de validação no QR Code.
define('VALIDATION_BASE_URL', 'https://app.assinadordosdespachantes.com.br/validate/');
// Define o caminho para a imagem do logo do ICP-Brasil.
define('ICP_LOGO_PATH', __DIR__. '/../private/assets/icp-logo.png'); // Você precisa adicionar essa imagem

// --- FUNÇÕES AUXILIARES ---

/**
 * Gera um código de validação único e criptograficamente seguro.
 * Formato: XXXXX-XXXXX-XXXXX-XXXXX
 * @return string O código de validação gerado.
 */
function generateValidationCode(): string {
    // Gera 10 bytes aleatórios seguros. [3]
    $bytes = random_bytes(10);
    // Converte para hexadecimal e maiúsculas, resultando em 20 caracteres.
    $hex = strtoupper(bin2hex($bytes));
    // Insere hifens para formatar o código.
    return implode('-', str_split($hex, 5));
}

/**
 * Extrai informações da assinatura digital de um arquivo PDF.
 * @param string $pdfPath O caminho para o arquivo PDF.
 * @return array|null Um array com 'signerName', 'signerCpf', 'signatureDate' ou null em caso de falha.
 */
function extractSignatureData(string $pdfPath):?array {
    $content = file_get_contents($pdfPath);
    if ($content === false) {
        return null;
    }

    // Regex para encontrar o último contêiner de assinatura PKCS#7 e a data de modificação. [4]
    $regex = '/\/Contents\s*<([a-fA-F0-9\s]+)>(?:.|\n)*?\/M\s*\(D:(\d{14})/';
    if (preg_match_all($regex, $content, $matches, PREG_SET_ORDER)) {
        // Pega a última assinatura encontrada
        $lastMatch = end($matches);
        $hexContents = preg_replace('/\s+/', '', $lastMatch[1]);
        $binaryContents = hex2bin($hexContents);

        // Formata a data da assinatura
        $dateString = $lastMatch[2];
        $dateTime = DateTime::createFromFormat('YmdHis', $dateString);
        $formattedDate = $dateTime? $dateTime->format('d/m/Y H:i:s') : 'Data inválida';

        // Prepara o contêiner PKCS#7 para leitura pelo OpenSSL. [4]
        $pem = "-----BEGIN PKCS7-----\n". chunk_split(base64_encode($binaryContents), 64, "\n"). "-----END PKCS7-----\n";
        
        $certificates =;
        if (openssl_pkcs7_read($pem, $certificates)) {
            if (!empty($certificates)) {
                // O primeiro certificado é geralmente o do assinante.
                $certData = openssl_x509_parse($certificates);
                if ($certData) {
                    $signerName = $certData['subject']['CN']?? 'Nome não encontrado';
                    
                    // O CPF no padrão ICP-Brasil geralmente está no serialNumber.
                    $signerCpf = 'CPF não encontrado';
                    if (isset($certData['subject']['serialNumber'])) {
                        // Aplica uma máscara para proteger a informação
                        $rawCpf = $certData['subject']['serialNumber'];
                        if (strlen($rawCpf) >= 9) {
                           $signerCpf = '***.'. substr($rawCpf, 3, 3). '.'. substr($rawCpf, 6, 3). '-**';
                        }
                    }

                    return;
                }
            }
        }
    }
    return null;
}

/**
 * Encerra o script com uma mensagem de erro formatada.
 * @param string $message A mensagem de erro a ser exibida.
 */
function exitWithError(string $message): void {
    http_response_code(400);
    die("Erro: ". htmlspecialchars($message));
}

// --- FLUXO PRINCIPAL ---

// 1. Validação da Requisição e do Arquivo
if ($_SERVER!== 'POST') {
    exitWithError("Método de requisição inválido. Use POST.");
}

if (!isset($_FILES['signedPdf']) ||!is_uploaded_file($_FILES['signedPdf']['tmp_name'])) {
    exitWithError("Nenhum arquivo foi enviado.");
}

$file = $_FILES['signedPdf'];

// Verifica erros de upload. [5, 6]
if ($file['error']!== UPLOAD_ERR_OK) {
    $errorMessages =;
    $errorMessage = $errorMessages[$file['error']]?? 'Erro desconhecido no upload.';
    exitWithError($errorMessage);
}

// Valida o tamanho do arquivo. [5]
if ($file['size'] > MAX_FILE_SIZE) {
    exitWithError("O arquivo é muito grande. O tamanho máximo é de ". (MAX_FILE_SIZE / 1024 / 1024). " MB.");
}

// Valida o tipo MIME do arquivo usando o conteúdo, não o que o navegador envia. [5, 7]
$finfo = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $finfo->file($file['tmp_name']);
if ($mimeType!== 'application/pdf') {
    exitWithError("Formato de arquivo inválido. Apenas PDFs são permitidos.");
}

// 2. Geração de Código e Armazenamento
$validationCode = generateValidationCode();

// Garante que os diretórios de armazenamento existem e são graváveis. [7]
foreach ( as $dir) {
    if (!is_dir($dir)) mkdir($dir, 0755, true);
    if (!is_writable($dir)) exitWithError("O diretório de armazenamento '{$dir}' não tem permissão de escrita.");
}

$newFilePath = UPLOAD_DIR. $validationCode. '.pdf';

// Move o arquivo enviado para o diretório seguro. [5, 6]
if (!move_uploaded_file($file['tmp_name'], $newFilePath)) {
    exitWithError("Falha ao mover o arquivo enviado. Verifique as permissões do servidor.");
}

// 3. Extração de Dados e Geração de Artefatos
$signatureData = extractSignatureData($newFilePath);
if ($signatureData === null) {
    // Se não conseguir extrair, remove o arquivo e informa o erro.
    unlink($newFilePath);
    exitWithError("Não foi possível extrair os dados da assinatura. O PDF pode não estar assinado corretamente ou o formato da assinatura não é suportado.");
}

// Gera o QR Code. [8, 9]
$validationUrl = VALIDATION_BASE_URL. $validationCode;
$qrCodePath = QR_TEMP_DIR. $validationCode. '.png';
QRcode::png($validationUrl, $qrCodePath, QR_ECLEVEL_L, 4);

// 4. Geração do Manifesto em PDF com TCPDF
try {
    $pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

    $pdf->SetCreator(PDF_CREATOR);
    $pdf->SetAuthor('Sistema de Validação');
    $pdf->SetTitle('Manifesto de Assinaturas - '. $validationCode);
    $pdf->setPrintHeader(false);
    $pdf->setPrintFooter(false);
    $pdf->AddPage();
    $pdf->SetFont('helvetica', '', 11);

    // Adiciona o logo do ICP-Brasil
    if (file_exists(ICP_LOGO_PATH)) {
        $pdf->Image(ICP_LOGO_PATH, 15, 15, 30, 0, 'PNG');
    }

    // Adiciona o QR Code
    if (file_exists($qrCodePath)) {
        $pdf->Image($qrCodePath, 170, 15, 25, 25, 'PNG');
    }

    // Títulos
    $pdf->SetFont('helvetica', 'B', 16);
    $pdf->Cell(0, 10, 'MANIFESTO DE ASSINATURAS', 0, 1, 'C', 0, '', 0, false, 'T', 'M');
    $pdf->Ln(15);

    // Corpo do Manifesto
    $pdf->SetFont('helvetica', '', 12);
    $pdf->Cell(0, 10, 'Código de validação: '. $validationCode, 0, 1, 'L');
    $pdf->Ln(5);
    
    $pdf->SetFont('helvetica', 'B', 12);
    $pdf->Cell(0, 10, 'Tipo de assinatura: Qualificada', 0, 1, 'L');
    $pdf->Ln(10);

    $pdf->SetFont('helvetica', '', 11);
    $pdf->MultiCell(0, 10, 'Esse documento foi assinado pelos seguintes signatários nas datas indicadas (Fuso horário de Brasília):', 0, 'L');
    $pdf->Ln(5);

    // Informações do signatário
    $html = '<div style="border-left: 3px solid #1abc9c; padding-left: 10px;">'.
            '<b>'. htmlspecialchars($signatureData['signerName']). '</b> ('. htmlspecialchars($signatureData['signerCpf']). ') em '. $signatureData. '<br>'.
            '<span style="font-size: 9pt; color: #555;">Assinado com certificado digital ICP-Brasil</span>'.
            '</div>';
    $pdf->writeHTML($html, true, false, true, false, '');
    $pdf->Ln(15);

    // Links de verificação
    $pdf->MultiCell(0, 10, 'Para verificar as assinaturas, acesse o link direto de validação deste documento:', 0, 'L');
    $pdf->SetTextColor(44, 62, 80);
    $pdf->SetFont('', 'U');
    $pdf->MultiCell(0, 5, $validationUrl, 0, 'L', false, 1, '', '', true, 0, true, true, 0, 'T', false);
    $pdf->Ln(10);
    
    $pdf->SetTextColor(0, 0, 0);
    $pdf->SetFont('', '');
    $pdf->MultiCell(0, 10, 'Ou acesse a consulta de documentos assinados disponível no link abaixo e informe o código de validação:', 0, 'L');
    $pdf->SetTextColor(44, 62, 80);
    $pdf->SetFont('', 'U');
    $pdf->MultiCell(0, 5, VALIDATION_BASE_URL, 0, 'L', false, 1, '', '', true, 0, true, true, 0, 'T', false);
    $pdf->Ln(15);

    // Aviso legal final
    $pdf->SetFont('helvetica', '', 9);
    $pdf->SetTextColor(127, 140, 141);
    $pdf->MultiCell(0, 10, 'Página destinada apenas ao download do arquivo original, a validação dos arquivos deve ser feita em https://validar.iti.gov.br/', 0, 'C');

    // Salva o manifesto em um arquivo temporário.
    $manifestoPath = MANIFEST_DIR. 'manifesto-'. $validationCode. '.pdf';
    $pdf->Output($manifestoPath, 'F');

} catch (Exception $e) {
    // Em caso de erro na geração do PDF, remove os arquivos criados e informa o erro.
    unlink($newFilePath);
    if (file_exists($qrCodePath)) unlink($qrCodePath);
    exitWithError("Ocorreu um erro ao gerar o manifesto: ". $e->getMessage());
}

// 5. Entrega do Arquivo e Limpeza
// Limpa o QR Code temporário
unlink($qrCodePath);

if (file_exists($manifestoPath)) {
    // Força o download do manifesto para o navegador do usuário.
    header('Content-Description: File Transfer');
    header('Content-Type: application/pdf');
    header('Content-Disposition: attachment; filename="manifesto-'. $validationCode. '.pdf"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: '. filesize($manifestoPath));
    flush(); // Garante que os cabeçalhos sejam enviados
    readfile($manifestoPath);
    
    // Remove o arquivo de manifesto do servidor após o download.
    unlink($manifestoPath);
    exit;
} else {
    exitWithError("O manifesto gerado não foi encontrado no servidor.");
}
