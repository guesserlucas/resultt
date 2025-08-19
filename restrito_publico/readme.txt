encritação utilizada StatiCrypt - https://translateabook.com/staticrypt/.

ORIGINAIS:
gerador_de_declarações.html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Declarações para Licitação</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Lora:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* Estilos personalizados */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f2f5;
        }
        .declaration-title {
            font-family: 'Lora', serif;
            font-weight: 700;
        }
        .declaration-body {
            font-family: 'Lora', serif;
            text-align: justify;
        }
        .header-bg {
            background-color: #ffffff;
        }
        .btn-primary {
            background-color: #005A8D; /* Azul do logo */
        }
        .btn-primary:hover {
            background-color: #004B74;
        }

        /* Estilos para impressão */
        @media print {
            body * {
                visibility: hidden;
            }
            #declarationsOutput, #declarationsOutput * {
                visibility: visible;
            }
            #declarationsOutput {
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
            }
            .no-print {
                display: none;
            }
            .declaration-card {
                page-break-after: always;
                border: none !important;
                box-shadow: none !important;
                margin-top: 0 !important;
            }
            .declaration-card:last-child {
                page-break-after: auto;
            }
        }
    </style>
</head>
<body class="text-gray-800">

    <!-- Cabeçalho com Logo -->
    <header class="header-bg shadow-md p-4 no-print">
        <div class="container mx-auto flex justify-between items-center">
            <img src="https://www.resulttcontabilidade.com.br/01.png" alt="Logo Resultt Contabilidade" class="h-12">
            <h1 class="text-2xl sm:text-3xl font-bold text-gray-700 hidden sm:block">Gerador de Declarações</h1>
        </div>
    </header>

    <div class="container mx-auto p-4 sm:p-6 md:p-8">
        <h2 class="text-center text-2xl font-bold text-gray-600 mb-6 no-print">Dados para Preenchimento</h2>

        <!-- Formulário de Entrada -->
        <div id="form-container" class="max-w-4xl mx-auto bg-white p-6 sm:p-8 rounded-lg shadow-lg no-print">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6">
                <!-- Coluna da Empresa -->
                <div class="space-y-4">
                    <h3 class="text-lg font-semibold text-gray-600 border-b pb-2">Dados da Empresa</h3>
                    <div>
                        <label for="cnpj" class="block text-sm font-medium text-gray-700">CNPJ</label>
                        <input type="text" id="cnpj" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" placeholder="Digite o CNPJ e aguarde">
                        <p id="cnpj-status" class="text-xs text-gray-500 mt-1 h-4"></p>
                    </div>
                    <div>
                        <label for="companyName" class="block text-sm font-medium text-gray-700">Nome da Empresa (Razão Social)</label>
                        <input type="text" id="companyName" class="mt-1 block w-full rounded-md border-gray-300 bg-gray-50 shadow-sm sm:text-sm" placeholder="Preenchido automaticamente" readonly>
                    </div>
                    <div>
                        <label for="companyAddress" class="block text-sm font-medium text-gray-700">Endereço Completo da Empresa</label>
                        <input type="text" id="companyAddress" class="mt-1 block w-full rounded-md border-gray-300 bg-gray-50 shadow-sm sm:text-sm" placeholder="Preenchido automaticamente" readonly>
                    </div>
                </div>

                <!-- Coluna do Representante -->
                <div class="space-y-4">
                     <h3 class="text-lg font-semibold text-gray-600 border-b pb-2">Dados do Representante Legal</h3>
                    <div>
                        <label for="repName" class="block text-sm font-medium text-gray-700">Nome do Representante</label>
                        <input type="text" id="repName" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" placeholder="Nome completo do representante">
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="repCpf" class="block text-sm font-medium text-gray-700">CPF</label>
                            <input type="text" id="repCpf" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" placeholder="000.000.000-00">
                        </div>
                        <div>
                            <label for="repRg" class="block text-sm font-medium text-gray-700">RG</label>
                            <input type="text" id="repRg" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" placeholder="Número do RG">
                        </div>
                    </div>
                     <div>
                        <label for="repRole" class="block text-sm font-medium text-gray-700">Cargo do Representante</label>
                        <input type="text" id="repRole" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" placeholder="Ex: Sócio-Administrador">
                    </div>
                </div>
                 <!-- Coluna do Edital -->
                <div class="space-y-4 md:col-span-2">
                     <h3 class="text-lg font-semibold text-gray-600 border-b pb-2">Dados da Licitação</h3>
                     <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <div class="sm:col-span-2">
                            <label for="publicBody" class="block text-sm font-medium text-gray-700">Nome do Órgão Público Contratante</label>
                            <input type="text" id="publicBody" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" placeholder="Ex: Prefeitura Municipal de...">
                        </div>
                        <div>
                            <label for="local" class="block text-sm font-medium text-gray-700">Local e Data</label>
                            <input type="text" id="local" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" placeholder="Ex: Florianópolis">
                        </div>
                        <div>
                            <label for="editalNumber" class="block text-sm font-medium text-gray-700">Nº do Edital/Processo</label>
                            <input type="text" id="editalNumber" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" placeholder="Ex: 123">
                        </div>
                        <div>
                            <label for="editalYear" class="block text-sm font-medium text-gray-700">Ano do Edital</label>
                            <input type="text" id="editalYear" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm" placeholder="Ex: 2025">
                        </div>
                     </div>
                </div>
            </div>

            <!-- Botões de Ação -->
            <div class="mt-8 flex flex-col sm:flex-row justify-end items-center space-y-4 sm:space-y-0 sm:space-x-4">
                <p id="error-message" class="text-red-600 text-sm h-4 text-left sm:text-right w-full"></p>
                <button id="generateButton" class="w-full sm:w-auto inline-flex justify-center py-2 px-6 border border-transparent shadow-sm text-sm font-medium rounded-md text-white btn-primary focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-500">
                    Gerar Declarações
                </button>
                 <button id="printButton" class="hidden w-full sm:w-auto inline-flex justify-center py-2 px-6 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-500">
                    Imprimir / Salvar PDF
                </button>
            </div>
        </div>

        <!-- Saída das Declarações -->
        <div id="declarationsOutput" class="mt-10 space-y-8">
            <!-- Os modelos de declaração serão inseridos aqui via JS -->
        </div>
    </div>

    <!-- Templates das Declarações (invisíveis inicialmente) -->
    <div id="declarationTemplates" class="hidden">
        
        <!-- 1. DECLARAÇÃO DE IDONEIDADE -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DE IDONEIDADE</h2>
            <p class="declaration-body leading-relaxed">
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ sob o nº <strong class="data-cnpj">____</strong>, com sede na <strong class="data-companyAddress">____</strong>, por intermédio de seu representante legal abaixo assinado, o(a) Sr.(a) <strong class="data-repName">____</strong>, portador(a) da Carteira de Identidade RG nº <strong class="data-repRg">____</strong> e inscrito(a) no CPF sob o nº <strong class="data-repCpf">____</strong>, no exercício do cargo de <strong class="data-repRole">____</strong>,
                <br><br>
                <strong>DECLARA</strong>, para os fins do Pregão/Edital nº <strong class="data-editalNumber">____</strong> e sob as penas da lei, em especial as previstas no Art. 299 do Código Penal (Falsidade Ideológica), que não se encontra suspensa de participar de licitação, nem foi declarada inidônea para licitar ou contratar com a Administração Pública Federal, Estadual, Distrital ou Municipal.
                <br><br>
                Declara, ainda, que até a presente data, inexistem fatos impeditivos para sua habilitação no presente certame, ciente da obrigatoriedade de declarar ocorrências posteriores.
                <br><br>
                Por ser a expressão da verdade, firma a presente.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-repRole">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

        <!-- 2. DECLARAÇÃO SOBRE TRABALHO DE MENOR -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-2">DECLARAÇÃO DE CUMPRIMENTO DO DISPOSTO NO INCISO XXXIII DO ART. 7º DA CONSTITUIÇÃO FEDERAL</h2>
            <p class="text-center text-sm mb-6">(DECLARAÇÃO SOBRE TRABALHO DE MENOR)</p>
            <p class="declaration-body leading-relaxed">
                <strong>Referência:</strong> Edital/Processo nº <strong class="data-editalNumber">____</strong>
                <br><br>
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ sob o nº <strong class="data-cnpj">____</strong>, com sede na <strong class="data-companyAddress">____</strong>, por intermédio de seu representante legal, o(a) Sr.(a) <strong class="data-repName">____</strong>, portador(a) da Carteira de Identidade RG nº <strong class="data-repRg">____</strong> e inscrito(a) no CPF sob o nº <strong class="data-repCpf">____</strong>,
                <br><br>
                <strong>DECLARA</strong>, para os fins do disposto no inciso V do art. 27 da Lei nº 8.666/1993 e no inciso VI do art. 68 da Lei nº 14.133/2021, e sob as penas da lei, que não emprega menor de dezoito anos em trabalho noturno, perigoso ou insalubre e não emprega menor de dezesseis anos em qualquer trabalho.
                <br><br>
                ( ) Ressalva: emprega menor, a partir de quatorze anos, na condição de aprendiz.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

        <!-- 3. DECLARAÇÃO DE CUMPRIMENTO DE RESERVA DE CARGOS -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DE CUMPRIMENTO DE RESERVA DE CARGOS</h2>
            <p class="declaration-body leading-relaxed">
                <strong>Referência:</strong> Edital/Processo nº <strong class="data-editalNumber">____</strong>
                <br><br>
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ sob o nº <strong class="data-cnpj">____</strong>, com sede na <strong class="data-companyAddress">____</strong>, por intermédio de seu representante legal, o(a) Sr.(a) <strong class="data-repName">____</strong>, portador(a) da Carteira de Identidade RG nº <strong class="data-repRg">____</strong> e inscrito(a) no CPF sob o nº <strong class="data-repCpf">____</strong>,
                <br><br>
                <strong>DECLARA</strong>, para os fins do disposto no inciso IV do art. 63 da Lei nº 14.133/2021 e sob as penas da lei, que cumpre as exigências de reserva de cargos prevista em lei para pessoa com deficiência e para reabilitado da Previdência Social, nos termos do Art. 93 da Lei nº 8.213, de 24 de julho de 1991.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>
        
        <!-- 4. DECLARAÇÃO DE INEXISTÊNCIA DE VÍNCULO COM SERVIDOR PÚBLICO -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DE INEXISTÊNCIA DE VÍNCULO COM SERVIDOR PÚBLICO</h2>
            <p class="declaration-body leading-relaxed">
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ sob o nº <strong class="data-cnpj">____</strong>, por intermédio de seu representante legal abaixo assinado,
                <br><br>
                <strong>DECLARA</strong>, sob as penas da lei, para os fins do Edital/Processo nº <strong class="data-editalNumber">____</strong>:
                <br><br>
                Que não possui em seu quadro societário, de diretores ou de funcionários, servidor ou dirigente do órgão ou entidade contratante ou responsável pela licitação.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

        <!-- 5. DECLARAÇÃO DE NÃO UTILIZAÇÃO DE TRABALHO DEGRADANTE OU FORÇADO -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DE NÃO UTILIZAÇÃO DE TRABALHO DEGRADANTE OU FORÇADO</h2>
            <p class="declaration-body leading-relaxed">
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ sob o nº <strong class="data-cnpj">____</strong>, com sede na <strong class="data-companyAddress">____</strong>, por intermédio de seu representante legal,
                <br><br>
                <strong>DECLARA</strong>, para os devidos fins e sob as penas da lei, que não possui em sua cadeia produtiva empregados executando trabalho degradante ou forçado, observando o disposto nos incisos III e IV do art. 1º e no inciso III do art. 5º da Constituição Federal.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

        <!-- 6. DECLARAÇÃO DE CUMPRIMENTO DA LGPD -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DE CUMPRIMENTO DA LEI GERAL DE PROTEÇÃO DE DADOS PESSOAIS (LEI Nº 13.709/2018)</h2>
            <p class="declaration-body leading-relaxed">
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ sob o nº <strong class="data-cnpj">____</strong>, por intermédio de seu representante legal abaixo assinado,
                <br><br>
                <strong>DECLARA</strong>, para todos os fins de direito e em relação ao contrato a ser firmado com <strong class="data-publicBody">____</strong>:
                <br><br>
                Ter pleno conhecimento das obrigações, deveres e responsabilidades impostos pela Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais - LGPD).
                <br><br>
                Que se compromete a tratar todos os dados pessoais a que tiver acesso em decorrência da execução do contrato estritamente para a finalidade do objeto contratado, sendo vedada qualquer utilização, reprodução ou compartilhamento para fins diversos.
                <br><br>
                Que adota medidas de segurança, técnicas e administrativas, aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado.
                <br><br>
                Que se responsabiliza integralmente, nos termos da lei, por quaisquer danos patrimoniais, morais, individuais ou coletivos que venha a causar aos titulares dos dados em decorrência da inobservância da LGPD.
                <br><br>
                Por ser verdade, firma a presente.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

        <!-- 7. DECLARAÇÃO DE LOCALIZAÇÃO -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DE LOCALIZAÇÃO</h2>
            <p class="declaration-body leading-relaxed">
                <strong>Referência:</strong> Edital de Licitação nº <strong class="data-editalNumber">____</strong> – <strong class="data-publicBody">____</strong>
                <br><br>
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ sob o nº <strong class="data-cnpj">____</strong>, com sede na <strong class="data-companyAddress">____</strong>, por intermédio de seu representante legal abaixo assinado, o(a) Sr.(a) <strong class="data-repName">____</strong>, portador(a) da Carteira de Identidade RG nº <strong class="data-repRg">____</strong> e inscrito(a) no CPF sob o nº <strong class="data-repCpf">____</strong>, no exercício do cargo de <strong class="data-repRole">____</strong>,
                <br><br>
                <strong>DECLARA</strong>, para os devidos fins de habilitação no certame em referência e sob as penas da lei, que o estabelecimento da empresa está localizado no endereço supracitado, abaixo da distância máxima da sede do licitante conforme exigido pelo edital.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong> (Carimbo do CNPJ)</p>
            </div>
        </div>

        <!-- 8. ATESTADO DE CAPACIDADE TÉCNICA -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">ATESTADO DE CAPACIDADE TÉCNICA</h2>
            <p class="declaration-body leading-relaxed">
                A <strong>[Nome da Empresa ou Órgão que está emitindo o atestado]</strong>, pessoa jurídica de direito [público/privado], inscrita no CNPJ sob o nº <strong>[CNPJ do Emissor]</strong>, com sede em <strong>[Endereço Completo do Emissor]</strong>, por intermédio de seu representante legal,
                <br><br>
                <strong>ATESTA</strong>, para os devidos fins e a quem possa interessar, que a empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ sob o nº <strong class="data-cnpj">____</strong>, com sede em <strong class="data-companyAddress">____</strong>, executou para esta instituição os seguintes serviços:
                <br><br>
                <strong>1. Objeto do Contrato:</strong> [Descrever o objeto do contrato executado].
                <br><br>
                <strong>2. Período de Execução:</strong> O contrato foi executado no período de [Data de Início] a [Data de Fim].
                <br><br>
                <strong>3. Avaliação dos Serviços:</strong> Atestamos que, durante toda a vigência do contrato, os serviços foram prestados de forma satisfatória, com bom desempenho operacional e cumprimento de todas as obrigações assumidas. Não constam em nossos registros, até a presente data, fatos que desabonem a conduta técnica ou comercial da referida empresa.
                <br><br>
                Por ser a expressão da verdade, firmamos o presente atestado.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong>[Nome da Empresa/Órgão Emissor]</strong></p>
                <p>Contato para verificação: Telefone: [Telefone do Emissor] E-mail: [E-mail do Emissor]</p>
            </div>
        </div>
        
        <!-- NOVAS DECLARAÇÕES INSERIDAS A PARTIR DAQUI -->

        <!-- 9. DECLARAÇÃO DO PORTE DA EMPRESA (ME/EPP) -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DO PORTE DA EMPRESA (MICROEMPRESA OU EMPRESA DE PEQUENO PORTE)</h2>
            <p class="declaration-body leading-relaxed">
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ nº <strong class="data-cnpj">____</strong>, por intermédio de seu representante legal o(a) Sr.(a) <strong class="data-repName">____</strong>, portador(a) da Carteira de Identidade nº <strong class="data-repRg">____</strong> e do CPF nº <strong class="data-repCpf">____</strong>, <strong>DECLARA</strong>, sob as penalidades da lei, que se enquadra como Microempresa ou Empresa de Pequeno Porte, nos termos do Art. 3º da Lei Complementar nº 123 de 14 de dezembro de 2006, estando apta a fruir os benefícios e vantagens legalmente instituídas por não se enquadrar em nenhuma das vedações legais impostas pelo § 4º do Art. 3º da Lei Complementar nº 123 de 14 de dezembro de 2006 e pelo Artigo 4º da Lei nº 14.133/2021.
                <br><br>
                Declaro, para fins da LC 123/2006 e suas alterações, sob as penalidades desta, ser:
                <div class="mt-4 space-y-2">
                    <div>
                        <input type="checkbox" id="me_checkbox" name="porte" class="h-4 w-4 text-sky-600 border-gray-300 rounded focus:ring-sky-500">
                        <label for="me_checkbox" class="ml-2"><strong>MICROEMPRESA</strong> – Receita Bruta anual igual ou inferior a R$ 360.000,00.</label>
                    </div>
                    <div>
                        <input type="checkbox" id="epp_checkbox" name="porte" class="h-4 w-4 text-sky-600 border-gray-300 rounded focus:ring-sky-500">
                        <label for="epp_checkbox" class="ml-2"><strong>EMPRESA DE PEQUENO PORTE</strong> – Receita Bruta anual superior a R$ 360.000,00 e igual ou inferior a R$ 4.800.000,00.</label>
                    </div>
                </div>
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

        <!-- 10. DECLARAÇÃO DE SUJEIÇÃO AO EDITAL E INEXISTÊNCIA DE FATOS IMPEDITIVOS -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DE SUJEIÇÃO ÀS CONDIÇÕES DO EDITAL E INEXISTÊNCIA DE FATOS IMPEDITIVOS</h2>
            <p class="declaration-body leading-relaxed">
                À<br>
                <strong class="data-publicBody">____</strong><br>
                Ref: Edital/Processo nº <strong class="data-editalNumber">____</strong>
                <br><br>
                Eu, <strong class="data-repName">____</strong>, portador(a) do RG nº <strong class="data-repRg">____</strong> e do CPF nº <strong class="data-repCpf">____</strong>, na qualidade de responsável legal da proponente <strong class="data-companyName">____</strong>, CNPJ <strong class="data-cnpj">____</strong>, <strong>DECLARO</strong> expressamente que me sujeito às condições estabelecidas no Edital acima citado e que acatarei integralmente qualquer decisão que venha a ser tomada pelo órgão licitante quanto à qualificação das proponentes.
                <br><br>
                <strong>DECLARO</strong>, ainda, para todos os fins de direito, a inexistência de fatos supervenientes impeditivos da habilitação ou que comprometam a idoneidade da proponente.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p>CPF: <strong class="data-repCpf">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

        <!-- 11. DECLARAÇÃO DE ELABORAÇÃO INDEPENDENTE DE PROPOSTA -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DE ELABORAÇÃO INDEPENDENTE DE PROPOSTA</h2>
            <p class="declaration-body leading-relaxed">
                A empresa <strong class="data-companyName">____</strong>, CNPJ <strong class="data-cnpj">____</strong>, através de seu representante legal <strong class="data-repName">____</strong>, para fins do disposto no Edital de Licitação nº <strong class="data-editalNumber">____</strong>, <strong>DECLARA</strong>, sob as penas da lei, em especial o art. 299 do Código Penal Brasileiro, que:
            </p>
            <ol class="declaration-body leading-relaxed list-alpha list-inside mt-4 space-y-2">
                <li>A proposta apresentada para participar do certame foi elaborada de maneira independente por este licitante, e o conteúdo da proposta não foi, no todo ou em parte, direta ou indiretamente, informado, discutido ou recebido de qualquer outro participante potencial ou de fato do referido processo licitatório, por qualquer meio ou por qualquer pessoa;</li>
                <li>A intenção de apresentar a proposta elaborada para participar do certame não foi informada, discutida ou recebida de qualquer outro participante potencial ou de fato, por qualquer meio ou por qualquer pessoa;</li>
                <li>Não tentou, por qualquer meio ou por qualquer pessoa, influir na decisão de qualquer outro participante potencial ou de fato quanto a participar ou não da referida licitação;</li>
                <li>O conteúdo da proposta apresentada não será, no todo ou em parte, direta ou indiretamente, comunicado ou discutido com qualquer outro participante potencial ou de fato antes da adjudicação do objeto da referida licitação;</li>
                <li>O conteúdo da proposta apresentada não foi, no todo ou em parte, direta ou indiretamente, informado, discutido ou recebido de qualquer integrante do(a) <strong class="data-publicBody">____</strong> antes da abertura oficial das propostas; e</li>
                <li>Está plenamente ciente do teor e da extensão desta declaração e que detém plenos poderes e informações para firmá-la.</li>
            </ol>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

        <!-- 12. DECLARAÇÃO DE PLENO ATENDIMENTO -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO DE PLENO ATENDIMENTO AOS REQUISITOS DE HABILITAÇÃO</h2>
            <p class="declaration-body leading-relaxed">
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ/MF nº <strong class="data-cnpj">____</strong>, sediada no endereço <strong class="data-companyAddress">____</strong>, por seu representante legal, <strong class="data-repName">____</strong>, CPF nº <strong class="data-repCpf">____</strong> e portador(a) do RG nº <strong class="data-repRg">____</strong>, que ao final subscreve, <strong>DECLARA EXPRESSAMENTE</strong> a quem interessar possa e para fins de atendimento do Edital/Processo nº <strong class="data-editalNumber">____</strong>, que:
                <br><br>
                Conhece na íntegra o Edital, está ciente e concorda com as condições impostas nele e em seus anexos, ao passo que se submete às condições nele estabelecidas, bem como de que a proposta apresentada compreende a integralidade dos custos para atendimento dos direitos trabalhistas assegurados na Constituição Federal, nas leis trabalhistas, nas normas infralegais, nas convenções coletivas de trabalho e nos termos de ajustamento de conduta vigentes na data de sua entrega em definitivo e que cumpre plenamente os requisitos de habilitação definidos no instrumento convocatório.
            </p>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

        <!-- 13. DECLARAÇÃO ÚNICA (MODELO CONSOLIDADO) -->
        <div class="declaration-card bg-white p-8 rounded-lg shadow-lg border border-gray-200">
            <h2 class="declaration-title text-center text-xl mb-6">DECLARAÇÃO ÚNICA DE HABILITAÇÃO</h2>
            <p class="declaration-body leading-relaxed">
                A empresa <strong class="data-companyName">____</strong>, inscrita no CNPJ/MF nº <strong class="data-cnpj">____</strong>, sediada no endereço <strong class="data-companyAddress">____</strong>, por seu representante legal, <strong class="data-repName">____</strong>, CPF nº <strong class="data-repCpf">____</strong> e portador(a) do RG nº <strong class="data-repRg">____</strong>, que ao final subscreve, <strong>DECLARA EXPRESSAMENTE</strong>, para fins de atendimento do Edital/Processo nº <strong class="data-editalNumber">____</strong>, que:
            </p>
            <ol class="declaration-body leading-relaxed list-alpha list-inside mt-4 space-y-2">
                <li>Não emprega menor de 18 anos em trabalho noturno, perigoso ou insalubre e não emprega menor de 16 anos, salvo menor, a partir de 14 anos, na condição de aprendiz, nos termos do artigo 7°, XXXIII, da Constituição;</li>
                <li>Não possui, em sua cadeia produtiva, empregados executando trabalho degradante ou forçado, observando o disposto nos incisos III e IV do art. 1º e no inciso III do art. 5º da Constituição Federal;</li>
                <li>Cumpre as exigências de reserva de cargos para pessoa com deficiência e para reabilitado da Previdência Social, previstas em lei e em outras normas específicas;</li>
                <li>Inexistem quaisquer fatos impeditivos de sua habilitação e que a mesma não foi declarada inidônea por Ato do Poder Público, ou que esteja temporariamente impedida de licitar, contratar ou transacionar com a Administração Pública ou quaisquer de seus órgãos descentralizados (inciso III e IV do art. 156 da Lei 14.133/2021);</li>
                <li>Não possui funcionário público no quadro societário da empresa;</li>
                <li>Está adequada à Lei Geral de Proteção de Dados (LGPD) – Lei nº 13.709/2018;</li>
                <li>Conhece na íntegra o Edital, está ciente e concorda com as condições impostas nele e em seus anexos, ao passo que se submete às condições nele estabelecidas, bem como de que a proposta apresentada compreende a integralidade dos custos para atendimento dos direitos trabalhistas assegurados na Constituição Federal, nas leis trabalhistas, nas normas infralegais, nas convenções coletivas de trabalho e nos termos de ajustamento de conduta vigentes na data de sua entrega em definitivo e que cumpre plenamente os requisitos de habilitação definidos no instrumento convocatório.</li>
            </ol>
            <p class="text-center mt-12"><span class="data-local">____</span>, <span class="data-date">____</span>.</p>
            <div class="mt-16 text-center">
                 <p class="border-t-2 border-gray-700 w-80 mx-auto pt-2">Assinatura</p>
                <p><strong class="data-repName">____</strong></p>
                <p><strong class="data-companyName">____</strong></p>
            </div>
        </div>

    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            // Seleção dos elementos do DOM
            const cnpjInput = document.getElementById('cnpj');
            const companyNameInput = document.getElementById('companyName');
            const companyAddressInput = document.getElementById('companyAddress');
            const repNameInput = document.getElementById('repName');
            const repCpfInput = document.getElementById('repCpf');
            const repRgInput = document.getElementById('repRg');
            const repRoleInput = document.getElementById('repRole');
            const editalNumberInput = document.getElementById('editalNumber');
            const editalYearInput = document.getElementById('editalYear');
            const publicBodyInput = document.getElementById('publicBody');
            const localInput = document.getElementById('local');
            
            const generateButton = document.getElementById('generateButton');
            const printButton = document.getElementById('printButton');
            const declarationsOutput = document.getElementById('declarationsOutput');
            const declarationTemplates = document.getElementById('declarationTemplates');
            const errorMessage = document.getElementById('error-message');
            const cnpjStatus = document.getElementById('cnpj-status');

            // Função para buscar dados do CNPJ na BrasilAPI
            cnpjInput.addEventListener('blur', async function() {
                const cnpj = this.value.replace(/\D/g, ''); // Remove caracteres não numéricos
                if (cnpj.length === 14) {
                    cnpjStatus.textContent = 'Buscando dados do CNPJ...';
                    cnpjStatus.classList.remove('text-red-500', 'text-green-500');
                    cnpjStatus.classList.add('text-blue-500');
                    try {
                        const response = await fetch(`https://brasilapi.com.br/api/cnpj/v1/${cnpj}`);
                        if (response.ok) {
                            const data = await response.json();
                            companyNameInput.value = data.razao_social || '';
                            const address = `${data.logradouro || ''}, ${data.numero || ''} - ${data.bairro || ''}, ${data.municipio || ''} - ${data.uf || ''}, CEP: ${data.cep || ''}`;
                            companyAddressInput.value = address;
                            cnpjStatus.textContent = 'Dados da empresa preenchidos.';
                            cnpjStatus.classList.remove('text-blue-500');
                            cnpjStatus.classList.add('text-green-500');
                        } else {
                            throw new Error('CNPJ não encontrado ou inválido.');
                        }
                    } catch (error) {
                        console.error('Erro ao buscar CNPJ:', error);
                        cnpjStatus.textContent = 'Não foi possível buscar os dados do CNPJ.';
                        cnpjStatus.classList.remove('text-blue-500', 'text-green-500');
                        cnpjStatus.classList.add('text-red-500');
                    }
                } else if (cnpj.length > 0) {
                    cnpjStatus.textContent = 'CNPJ deve conter 14 dígitos.';
                    cnpjStatus.classList.add('text-red-500');
                } else {
                     cnpjStatus.textContent = '';
                }
            });

            // Função para gerar as declarações
            generateButton.addEventListener('click', function() {
                // Coleta dos valores dos inputs
                const data = {
                    cnpj: cnpjInput.value,
                    companyName: companyNameInput.value,
                    companyAddress: companyAddressInput.value,
                    repName: repNameInput.value,
                    repCpf: repCpfInput.value,
                    repRg: repRgInput.value,
                    repRole: repRoleInput.value,
                    editalNumber: editalNumberInput.value,
                    editalYear: editalYearInput.value,
                    publicBody: publicBodyInput.value,
                    local: localInput.value,
                };
                
                // Validação
                const requiredFields = ['cnpj', 'companyName', 'companyAddress', 'repName', 'repCpf', 'repRg', 'repRole', 'editalNumber', 'publicBody', 'local'];
                const missingField = requiredFields.find(field => !data[field]);

                if (missingField) {
                    errorMessage.textContent = 'Por favor, preencha todos os campos do formulário.';
                    try {
                        document.getElementById(missingField).focus();
                    } catch(e) {
                        console.error("Could not focus on missing field:", missingField);
                    }
                    return;
                }
                errorMessage.textContent = '';

                // Preenchimento das declarações
                declarationsOutput.innerHTML = ''; // Limpa saídas anteriores
                const templates = declarationTemplates.querySelectorAll('.declaration-card');
                
                const now = new Date();
                const dateString = now.toLocaleDateString('pt-BR', { day: '2-digit', month: 'long', year: 'numeric' });

                templates.forEach(template => {
                    const clone = template.cloneNode(true);
                    
                    // Preenche os dados nos elementos correspondentes
                    clone.querySelectorAll('.data-cnpj').forEach(el => el.textContent = data.cnpj);
                    clone.querySelectorAll('.data-companyName').forEach(el => el.textContent = data.companyName);
                    clone.querySelectorAll('.data-companyAddress').forEach(el => el.textContent = data.companyAddress);
                    clone.querySelectorAll('.data-repName').forEach(el => el.textContent = data.repName);
                    clone.querySelectorAll('.data-repCpf').forEach(el => el.textContent = data.repCpf);
                    clone.querySelectorAll('.data-repRg').forEach(el => el.textContent = data.repRg);
                    clone.querySelectorAll('.data-repRole').forEach(el => el.textContent = data.repRole);
                    clone.querySelectorAll('.data-editalNumber').forEach(el => el.textContent = `${data.editalNumber}/${data.editalYear || new Date().getFullYear()}`);
                    clone.querySelectorAll('.data-publicBody').forEach(el => el.textContent = data.publicBody);
                    clone.querySelectorAll('.data-local').forEach(el => el.textContent = data.local);
                    clone.querySelectorAll('.data-date').forEach(el => el.textContent = dateString);

                    declarationsOutput.appendChild(clone);
                });

                printButton.classList.remove('hidden');
                declarationsOutput.scrollIntoView({ behavior: 'smooth' });
            });

            // Função para imprimir
            printButton.addEventListener('click', function() {
                window.print();
            });
        });
    </script>

</body>
</html>

declaracao_situacao_financeira.html

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Declaração de Situação Financeira - Resultt Contabilidade</title>
    <style>
        /* Estilos Gerais */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #eef2f5;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
            box-sizing: border-box;
        }

        /* Container Principal */
        .container {
            width: 100%;
            max-width: 900px;
            margin: auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 25px rgba(0, 40, 100, 0.12);
            border-top: 5px solid #0056b3;
        }

        /* Cabeçalho com Logo */
        .header {
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 1px solid #dee2e6;
            padding-bottom: 20px;
        }

        .header img {
            max-width: 280px;
            margin-bottom: 10px;
        }

        .header h1 {
            font-size: 1.8em;
            color: #003366;
            margin: 0;
        }

        /* Estilos de Seção */
        .section {
            margin-bottom: 25px;
        }

        .section h2 {
            font-size: 1.4em;
            color: #0056b3;
            border-bottom: 2px solid #0056b3;
            padding-bottom: 8px;
            margin-bottom: 20px;
        }

        /* Grupos de Formulário */
        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
        }

        .form-group label {
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
        }

        .form-group input {
            width: 100%;
            padding: 12px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 1em;
            transition: border-color 0.3s, box-shadow 0.3s;
        }

        .form-group input:focus {
            border-color: #0056b3;
            box-shadow: 0 0 8px rgba(0, 86, 179, 0.2);
            outline: none;
        }
        
        .form-group input[readonly] {
            background-color: #f0f0f0;
            cursor: not-allowed;
        }

        /* Botões */
        .btn {
            background-color: #007bff;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1em;
            font-weight: 600;
            transition: background-color 0.3s, transform 0.2s;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .btn:hover {
            background-color: #0056b3;
            transform: translateY(-2px);
        }
        
        .btn-secondary {
            background-color: #6c757d;
        }
        
        .btn-secondary:hover {
            background-color: #5a6268;
        }

        .button-group {
            display: flex;
            gap: 15px;
            margin-top: 20px;
            justify-content: center;
        }

        /* Tabela de Resultados */
        .results-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        .results-table th, .results-table td {
            border: 1px solid #dee2e6;
            padding: 12px;
            text-align: left;
        }

        .results-table th {
            background-color: #f8f9fa;
            font-weight: 600;
        }

        .results-table td {
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .status-ok { color: #28a745; }
        .status-fail { color: #dc3545; }

        /* Seção do Relatório Gerado */
        #report {
            margin-top: 40px;
            border: 1px solid #ccc;
            padding: 30px;
            display: none;
            background-color: #fff;
        }

        .report-header {
            text-align: center;
            font-weight: bold;
            font-size: 1.5em;
            margin-bottom: 30px;
        }

        #report p {
            line-height: 1.8;
            text-align: justify;
            font-size: 1.1em;
        }

        .signatures {
            margin-top: 80px;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 20px;
        }

        .signature-block {
            text-align: center;
            width: 300px;
        }
        
        .signature-block p {
            margin: 0;
            font-size: 1em;
            text-align: center;
        }

        .signature-line {
            border-top: 1px solid #000;
            margin-top: 60px;
            width: 100%;
        }

        /* Estilos Otimizados para Impressão em 1 Página A4 Retrato */
        @media print {
            @page {
                size: A4 portrait;
                margin: 2cm; /* Margem padrão para documentos A4 */
            }

            body {
                background-color: #fff;
                margin: 0;
                padding: 0;
                font-size: 11pt; /* Reduzido para caber mais conteúdo */
                -webkit-print-color-adjust: exact; /* Garante a impressão de cores no Chrome/Safari */
                print-color-adjust: exact;
            }

            /* Esconde o formulário, o título principal e os botões */
            .form-section,
            .button-group,
            .container > .header {
                display: none;
            }
            
            /* Reseta os estilos do container para impressão */
            .container {
                box-shadow: none;
                border: none;
                padding: 0;
                width: 100%;
                max-width: 100%;
            }

            /* Garante que a seção do relatório seja exibida e ocupe a página */
            #report {
                display: block !important;
                margin: 0;
                padding: 0;
                border: none;
                width: 100%;
            }
            
            #report .header img {
                max-width: 200px; /* Reduz um pouco o logo na impressão */
            }
            
            #report .report-header {
                font-size: 1.3em; /* Reduz o título do relatório */
                margin-bottom: 20px;
            }

            #report p {
                line-height: 1.5; /* Reduz o espaçamento entre linhas */
                text-align: justify;
                font-size: 1em; /* Garante que o p herde o 11pt do body */
                margin: 1em 0; /* Ajusta a margem do parágrafo */
            }

            .results-table th, .results-table td {
                padding: 8px; /* Reduz o padding da tabela */
            }

            /* Evita quebras de página dentro de elementos importantes */
            .results-table, .signatures {
                page-break-inside: avoid;
            }

            .signatures {
                margin-top: 2.5cm; /* Reduzido para evitar quebra de página */
                page-break-before: auto; /* Garante que não force uma quebra antes se não for necessário */
            }
            
            .signature-line {
                margin-top: 40px; /* Reduz o espaço acima da linha de assinatura */
            }
        }
    </style>
</head>
<body>

<div class="container">
    <header class="header">
        <img src="https://www.resulttcontabilidade.com.br/01.png" alt="Logo Resultt Contabilidade">
        <h1>Gerador de Declaração de Situação Financeira</h1>
    </header>

    <main class="form-section">
        <input type="hidden" id="cidadeEmpresa"> <!-- Campo oculto para guardar a cidade -->
        <section class="section">
            <h2>1. Dados da Empresa</h2>
            <div class="form-grid">
                <div class="form-group">
                    <label for="cnpj">CNPJ</label>
                    <input type="text" id="cnpj" placeholder="Apenas números">
                </div>
                <div class="form-group" style="justify-content: flex-end;">
                    <button class="btn" onclick="buscarCNPJ()">Buscar Dados via API</button>
                </div>
            </div>
            <div class="form-grid" style="margin-top: 20px;">
                <div class="form-group">
                    <label for="razaoSocial">Razão Social</label>
                    <input type="text" id="razaoSocial" readonly>
                </div>
                <div class="form-group">
                    <label for="endereco">Endereço</label>
                    <input type="text" id="endereco" readonly>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>2. Dados dos Responsáveis</h2>
             <div class="form-grid">
                <div class="form-group">
                    <label for="contador">Nome do Contador</label>
                    <input type="text" id="contador">
                </div>
                <div class="form-group">
                    <label for="cpfContador">CPF do Contador</label>
                    <input type="text" id="cpfContador">
                </div>
                <div class="form-group">
                    <label for="crcContador">CRC do Contador (com UF)</label>
                    <input type="text" id="crcContador" placeholder="Ex: CRC/SP 123456/O-7">
                </div>
                <div class="form-group">
                    <label for="repLegal">Nome do Representante Legal</label>
                    <input type="text" id="repLegal">
                </div>
                <div class="form-group">
                    <label for="cpfRepLegal">CPF do Representante Legal</label>
                    <input type="text" id="cpfRepLegal">
                </div>
                 <div class="form-group">
                    <label for="cargoRepLegal">Cargo do Representante Legal</label>
                    <input type="text" id="cargoRepLegal">
                </div>
            </div>
        </section>

        <section class="section">
            <h2>3. Dados para Cálculo dos Índices</h2>
            <div class="form-grid">
                <div class="form-group">
                    <label for="dataFechamento">Data de Fechamento do Balanço</label>
                    <input type="date" id="dataFechamento">
                </div>
                <div class="form-group">
                    <label for="ativoCirculante">Ativo Circulante</label>
                    <input type="number" id="ativoCirculante" placeholder="0.00" oninput="calcularIndices()">
                </div>
                <div class="form-group">
                    <label for="passivoCirculante">Passivo Circulante</label>
                    <input type="number" id="passivoCirculante" placeholder="0.00" oninput="calcularIndices()">
                </div>
                <div class="form-group">
                    <label for="ativoNaoCirculante">Ativo Não Circulante</label>
                    <input type="number" id="ativoNaoCirculante" placeholder="0.00" oninput="calcularIndices()">
                </div>
                <div class="form-group">
                    <label for="passivoNaoCirculante">Passivo Não Circulante</label>
                    <input type="number" id="passivoNaoCirculante" placeholder="0.00" oninput="calcularIndices()">
                </div>
                <div class="form-group">
                    <label for="ativoPermanente">Ativo Permanente (Imobilizado, Investimentos, Intangível)</label>
                    <input type="number" id="ativoPermanente" placeholder="0.00" oninput="calcularIndices()">
                </div>
            </div>
            
            <h3>Resultados dos Índices</h3>
            <table class="results-table">
                <thead>
                    <tr>
                        <th>Índice Financeiro</th>
                        <th>Resultado</th>
                        <th>Condição de Habilitação (>= 1.00)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Índice de Liquidez Corrente (ILC)</td>
                        <td id="resultadoILC">0.00</td>
                        <td id="statusILC">-</td>
                    </tr>
                    <tr>
                        <td>Índice de Liquidez Geral (ILG)</td>
                        <td id="resultadoILG">0.00</td>
                        <td id="statusILG">-</td>
                    </tr>
                    <tr>
                        <td>Índice de Solvência Geral (ISG)</td>
                        <td id="resultadoISG">0.00</td>
                        <td id="statusISG">-</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <div class="button-group">
            <button class="btn" onclick="gerarRelatorio()">Gerar Declaração</button>
            <button class="btn btn-secondary" onclick="window.print()">Imprimir</button>
        </div>
    </main>

    <section id="report">
        <header class="header">
            <img src="https://www.resulttcontabilidade.com.br/01.png" alt="Logo Resultt Contabilidade">
        </header>
        <h2 class="report-header">DECLARAÇÃO DE BOA SITUAÇÃO FINANCEIRA</h2>
        <p>
            A empresa <strong id="reportRazaoSocial"></strong>, inscrita no CNPJ sob o nº <strong id="reportCnpj"></strong>, com sede em <strong id="reportEndereco"></strong>, declara, para os devidos fins, sob as penas da Lei, que goza de boa situação financeira, conforme apurado em seu Balanço Patrimonial encerrado em <strong id="reportDataFechamento"></strong>.
        </p>
        <p>
            A presente declaração é fundamentada nos seguintes índices financeiros, os quais atendem às exigências de habilitação, apresentando resultado igual ou superior a 1,00 (um):
        </p>
        
        <table class="results-table">
             <thead>
                <tr>
                    <th>Índice Financeiro</th>
                    <th>Resultado Apurado</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Índice de Liquidez Corrente (ILC)</td>
                    <td id="reportILC"></td>
                </tr>
                <tr>
                    <td>Índice de Liquidez Geral (ILG)</td>
                    <td id="reportILG"></td>
                </tr>
                <tr>
                    <td>Índice de Solvência Geral (ISG)</td>
                    <td id="reportISG"></td>
                </tr>
            </tbody>
        </table>

        <p>
            Por ser a expressão da verdade, firmamos a presente declaração.
        </p>
        <p style="text-align: center; margin-top: 20px;">
            <span id="reportLocalData"></span>
        </p>

        <div class="signatures">
            <div class="signature-block">
                <div class="signature-line"></div>
                <p><strong id="reportRepLegal"></strong></p>
                <p><span id="reportCargoRepLegal"></span></p>
                <p>CPF: <span id="reportCpfRepLegal"></span></p>
            </div>
            <div class="signature-block">
                <div class="signature-line"></div>
                <p><strong id="reportContador"></strong></p>
                <p>Contador(a)</p>
                <p><span id="reportCrcContador"></span></p>
                <p>CPF: <span id="reportCpfContador"></span></p>
            </div>
        </div>
    </section>
</div>

<script>
    // Função para buscar dados do CNPJ usando a BrasilAPI
    async function buscarCNPJ() {
        let cnpj = document.getElementById('cnpj').value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (cnpj.length !== 14) {
            alert('Por favor, digite um CNPJ válido com 14 dígitos.');
            return;
        }

        const url = `https://brasilapi.com.br/api/cnpj/v1/${cnpj}`;
        
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Erro na API: ${response.statusText}`);
            }
            const data = await response.json();
            
            document.getElementById('razaoSocial').value = data.razao_social || '';
            const endereco = `${data.logradouro}, ${data.numero}, ${data.bairro}, ${data.municipio} - ${data.uf}, CEP: ${data.cep}`;
            document.getElementById('endereco').value = endereco;
            document.getElementById('cidadeEmpresa').value = data.municipio || ''; // Guarda a cidade no campo oculto

        } catch (error) {
            alert('Não foi possível consultar o CNPJ. Verifique o número digitado ou tente novamente mais tarde.');
            console.error('Erro ao buscar CNPJ:', error);
        }
    }

    // Função para calcular os índices financeiros
    function calcularIndices() {
        const ac = parseFloat(document.getElementById('ativoCirculante').value) || 0;
        const pc = parseFloat(document.getElementById('passivoCirculante').value) || 0;
        const anc = parseFloat(document.getElementById('ativoNaoCirculante').value) || 0;
        const pnc = parseFloat(document.getElementById('passivoNaoCirculante').value) || 0;
        const ap = parseFloat(document.getElementById('ativoPermanente').value) || 0;

        // Cálculo ILC
        const ilc = pc > 0 ? (ac / pc) : 0;
        document.getElementById('resultadoILC').textContent = ilc.toFixed(2);
        updateStatus('statusILC', ilc);

        // Cálculo ILG (fórmula atualizada)
        const ilg = (pc + pnc) > 0 ? ((ac + anc - ap) / (pc + pnc)) : 0;
        document.getElementById('resultadoILG').textContent = ilg.toFixed(2);
        updateStatus('statusILG', ilg);

        // Cálculo ISG 
        const isg = (pc + pnc) > 0 ? ((ac + anc) / (pc + pnc)) : 0;
        document.getElementById('resultadoISG').textContent = isg.toFixed(2);
        updateStatus('statusISG', isg);
    }
    
    // Função auxiliar para atualizar o status de habilitação
    function updateStatus(elementId, value) {
        const el = document.getElementById(elementId);
        if (value >= 1) {
            el.textContent = 'Habilitado';
            el.className = 'status-ok';
        } else {
            el.textContent = 'Inabilitado';
            el.className = 'status-fail';
        }
    }

    // Função para gerar o relatório
    function gerarRelatorio() {
        // Validação de campos obrigatórios
        const campos = [
            'cnpj', 'razaoSocial', 'endereco', 'contador', 'cpfContador', 
            'crcContador', 'repLegal', 'cpfRepLegal', 'cargoRepLegal',
            'dataFechamento', 'ativoCirculante', 'passivoCirculante', 'ativoNaoCirculante', 
            'passivoNaoCirculante', 'ativoPermanente'
        ];
        
        for (const campo of campos) {
            if (!document.getElementById(campo).value) {
                alert(`Por favor, preencha o campo: ${document.querySelector(`label[for=${campo}]`).textContent}`);
                return;
            }
        }
        
        // Transferir dados para a declaração
        document.getElementById('reportRazaoSocial').textContent = document.getElementById('razaoSocial').value;
        document.getElementById('reportCnpj').textContent = document.getElementById('cnpj').value;
        document.getElementById('reportEndereco').textContent = document.getElementById('endereco').value;
        document.getElementById('reportRepLegal').textContent = document.getElementById('repLegal').value;
        document.getElementById('reportCargoRepLegal').textContent = document.getElementById('cargoRepLegal').value;
        document.getElementById('reportCpfRepLegal').textContent = document.getElementById('cpfRepLegal').value;
        document.getElementById('reportContador').textContent = document.getElementById('contador').value;
        document.getElementById('reportCrcContador').textContent = document.getElementById('crcContador').value;
        document.getElementById('reportCpfContador').textContent = document.getElementById('cpfContador').value;
        
        // Formatar e transferir a data de fechamento
        const dataFechamentoRaw = document.getElementById('dataFechamento').value;
        const [ano, mes, dia] = dataFechamentoRaw.split('-');
        const dataFechamentoFormatada = `${dia}/${mes}/${ano}`;
        document.getElementById('reportDataFechamento').textContent = dataFechamentoFormatada;


        // Transferir resultados dos índices
        document.getElementById('reportILC').textContent = document.getElementById('resultadoILC').textContent;
        document.getElementById('reportILG').textContent = document.getElementById('resultadoILG').textContent;
        document.getElementById('reportISG').textContent = document.getElementById('resultadoISG').textContent;

        // Gerar local e data usando a cidade da empresa
        const hoje = new Date();
        const opcoesData = { year: 'numeric', month: 'long', day: 'numeric' };
        const cidade = document.getElementById('cidadeEmpresa').value; 
        document.getElementById('reportLocalData').textContent = `${cidade}, ${hoje.toLocaleDateString('pt-BR', opcoesData)}.`;

        // Exibir a declaração
        document.getElementById('report').style.display = 'block';
        
        // Rolar a página para a declaração
        document.getElementById('report').scrollIntoView({ behavior: 'smooth' });
    }

</script>

</body>
</html>

ricms_sc_.html

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta Tributária RICMS/SC - Resultt Contabilidade</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f2f5;
        }
        /* Cor primária inspirada na imagem - Laranja */
        .bg-primary {
            background-color: #f28524;
        }
        .text-primary {
            color: #f28524;
        }
        .border-primary {
            border-color: #f28524;
        }
        .btn-primary {
            background-color: #f28524;
            color: white;
            transition: background-color 0.3s ease;
        }
        .btn-primary:hover {
            background-color: #e67e22;
        }
        /* Estilo para o spinner de carregamento */
        .loader {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #f28524;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .prose h2 {
            color: #f28524;
            font-weight: 600;
        }
        .focus\:ring-primary:focus {
            --tw-ring-color: #f28524;
        }
    </style>
</head>
<body class="pt-8 md:pt-12">

    <!-- Conteúdo Principal -->
    <main class="container mx-auto px-4">
        <div class="max-w-3xl mx-auto bg-white p-6 md:p-10 rounded-xl shadow-lg border border-gray-200">
            
            <div class="text-center mb-8">
                <img src="https://www.resulttcontabilidade.com.br/01.png" alt="Logo Resultt Contabilidade" class="h-16 mx-auto mb-6" onerror="this.onerror=null;this.src='https://placehold.co/250x60/ffffff/f28524?text=Resultt';">
                <h1 class="text-2xl md:text-3xl font-bold text-primary">Consulta de Tratamento Tributário</h1>
                <p class="text-gray-600 mt-2">Pesquise por NCM ou descrição do produto no RICMS/SC</p>
            </div>

            <!-- Aviso Legal -->
            <div class="bg-orange-50 p-4 rounded-lg mb-8 text-center border border-orange-200">
                <p class="text-sm text-orange-800">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block mr-1 -mt-px text-orange-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <strong>Aviso Legal:</strong> O sistema utiliza Inteligência Artificial para levantamento de dados e pode estar sujeito a erros. Indicamos a verificação da base legal.
                </p>
            </div>

            <!-- Formulário de Busca -->
            <div class="flex flex-col sm:flex-row gap-3">
                <input type="text" id="searchInput" class="flex-grow w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-primary transition-colors" placeholder="Digite o NCM ou a descrição do produto...">
                <button id="searchButton" class="btn-primary font-semibold px-6 py-3 rounded-lg shadow-md hover:shadow-lg w-full sm:w-auto flex items-center justify-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block mr-2" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
                    </svg>
                    Buscar
                </button>
            </div>

            <!-- Botão para o Regulamento -->
            <div class="text-center mt-6 mb-6">
                <a href="https://legislacao.sef.sc.gov.br/consulta/views/Publico/Frame.aspx?x=/Cabecalhos/frame_ricms_01_00_00.htm" target="_blank" rel="noopener noreferrer" class="inline-flex items-center text-sm font-medium text-gray-600 hover:text-primary transition-colors duration-200">
                    Acessar Regulamento Completo (RICMS/SC)
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                </a>
            </div>

            <!-- Área de Resultados -->
            <div id="results">
                <div id="placeholder" class="text-center text-gray-500 py-10 border-t pt-8">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 mx-auto text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                    <p class="mt-4 font-medium">Os resultados da sua busca aparecerão aqui.</p>
                </div>
                <div id="loader" class="hidden flex-col items-center justify-center py-10 border-t pt-8">
                    <div class="loader"></div>
                    <p class="mt-4 text-primary font-semibold">Buscando informações... Por favor, aguarde.</p>
                </div>
                <div id="error" class="hidden text-center text-red-600 bg-red-50 p-4 rounded-lg border-t pt-8">
                    <p class="font-bold">Ocorreu um erro!</p>
                    <p id="errorMessage" class="text-sm">Não foi possível processar a sua solicitação. Tente novamente.</p>
                </div>
                <div id="resultContent" class="prose max-w-none text-gray-800 border-t pt-6"></div>
            </div>
        </div>
    </main>

    <!-- Rodapé -->
    <footer class="text-center py-8 mt-4">
        <p class="text-gray-500 text-sm">&copy; <span id="year"></span> Resultt Contabilidade. Todos os direitos reservados.</p>
    </footer>

    <script>
        // Define o ano atual no rodapé
        document.getElementById('year').textContent = new Date().getFullYear();

        // Elementos do DOM
        const searchButton = document.getElementById('searchButton');
        const searchInput = document.getElementById('searchInput');
        const resultsContainer = document.getElementById('results');
        const placeholder = document.getElementById('placeholder');
        const loader = document.getElementById('loader');
        const errorContainer = document.getElementById('error');
        const errorMessage = document.getElementById('errorMessage');
        const resultContent = document.getElementById('resultContent');

        // Adiciona evento de clique ao botão de busca
        searchButton.addEventListener('click', performSearch);
        
        // Permite buscar pressionando Enter
        searchInput.addEventListener('keyup', (event) => {
            if (event.key === 'Enter') {
                performSearch();
            }
        });

        /**
         * Função principal que executa a busca
         */
        async function performSearch() {
            const query = searchInput.value.trim();
            if (!query) {
                showError("Por favor, digite um NCM ou descrição para buscar.");
                return;
            }

            showLoading();

            try {
                // Monta o prompt para a API do Gemini
                const prompt = `
                   Use como contexto EXCLUSIVO o seguinte conteúdo:
				   
"DIFERIMENTO:
NCM;DESCRICAO;DIFERIMENTO;OUTRAS PARTICULARIDADES;BASE LEGAL
2302;CAMA DE AVIARIO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;QUANDO DESTINADAS A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA;ANEXO 3 ART 3 I
2302;CASCA DE ARROZ;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;QUANDO DESTINADAS A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA;ANEXO 3 ART 3 II
0903;ERVA-MATE EM FOLHA OU CANCHEADA;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;QUANDO DESTINADAS A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA;ANEXO 3 ART 3 III
1106;FARINHA GROSSA DE MANDIOCA;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;QUANDO DESTINADAS A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA;ANEXO 3 ART 3 IV
1106;RASPA LEVE OU PESADA DE MANDIOCA;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;QUANDO DESTINADAS A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUaria;ANEXO 3 ART 3 IV
0401;LEITE FRESCO PASTEURIZADO OU NAO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;QUANDO DESTINADAS A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA;ANEXO 3 ART 3 V
0402;LEITE RECONSTITUIDO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;QUANDO DESTINADAS A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA;ANEXO 3 ART 3 V
GERAL;PRODUTO ORIGINADO DA ATIVIDADE AGROPECUARIA OU EXTRATIVA VEGETAL OU MINERAL EM ESTADO NATURAL;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;QUANDO DESTINADAS A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA;ANEXO 3 ART 4 I
4402;CARVAO VEGETAL EXTRAIDO DE FLORESTAS CULTIVADAS;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;DESTINADO A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA OPERACAO ACOBERTADA POR GUIA FLORESTAL;ANEXO 3 ART 4 II
4401;LENHA EXTRAIDA DE FLORESTAS CULTIVADAS;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;DESTINADO A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA OPERACAO ACOBERTADA POR GUIA FLORESTAL;ANEXO 3 ART 4 II
4403;MADEIRAS EM TORAS EXTRAIDAS DE FLORESTAS CULTIVADAS;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;DESTINADO A COMERCIALIZACAO INDUSTRIALIZACAO OU ATIVIDADE AGROPECUARIA OPERACAO ACOBERTADA POR GUIA FLORESTAL;ANEXO 3 ART 4 II
0102;GADO BOVINO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;COM DESTINO A ESTABELECIMENTO ABATEDOR;ANEXO 3 ART 4 III A
0102;GADO BUFALINO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;COM DESTINO A ESTABELECIMENTO ABATEDOR;ANEXO 3 ART 4 III A
0102;GADO BOVINO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;COM DESTINO A OUTRO ESTABELECIMENTO PECUARISTA;ANEXO 3 ART 4 III B
0102;GADO BUFALINO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;COM DESTINO A OUTRO ESTABELECIMENTO PECUARISTA;ANEXO 3 ART 4 III B
0102;GADO BOVINO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;COM DESTINO A OUTRO ESTABELECIMENTO DO MESMO TITULAR LOCALIZADO NO MESMO MUNICIPIO OU EM MUNICIPIO ADJACENTE;ANEXO 3 ART 4 III C
0102;GADO BUFALINO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA DE ESTABELECIMENTO AGROPECUARIO;COM DESTINO A OUTRO ESTABELECIMENTO DO MESMO TITULAR LOCALIZADO NO MESMO MUNICIPIO OU EM MUNICIPIO ADJACENTE;ANEXO 3 ART 4 III C
2500;SUBSTANCIAS MINERAIS EM BRUTO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;DESTINADAS A INDUSTRIALIZACAO OU UTILIZACAO COMO MATERIA-PRIMA EM PROCESSO INDUSTRIAL;ANEXO 3 ART 5
2701;CARVAO MINERAL;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;DESTINATARIO FOR EMPRESA CONCESSIONARIA DE SERVICO PUBLICO PRODUTORA DE ENERGIA ELETRICA;ANEXO 3 ART 6 I
2701;CARVAO MINERAL;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;DESTINATARIO FOR ESTABELECIMENTO PRODUTOR INSCRITO NO RSP;ANEXO 3 ART 6 II
2701;CARVAO MINERAL;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;DESTINATARIO FOR FORNECEDOR DE EMPRESA CONCESSIONARIA DE SERVICO PUBLICO PRODUTORA DE ENERGIA ELETRICA;ANEXO 3 ART 6 III
GERAL;MERCADORIAS PERTENCENTES A TERCEIROS DE ESTABELECIMENTO DE EMPRESA DE TRANSPORTE;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;DESDE QUE O REMETENTE ESTEJA EM SC E POR CONTA E ORDEM DESTA;ANEXO 3 ART 7 VIII
4400;MADEIRA E PRODUTOS RESULTANTES DE SUA TRANSFORMACAO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;ENTRE ESTABELECIMENTOS INSCRITOS NO CCICMS LOCALIZADOS NA ZONA DE PROCESSAMENTO FLORESTAL ZPF;ANEXO 3 ART 7 IX
NA;SERVICOS PRESTADOS NO RETORNO DE MERCADORIA RECEBIDA PARA CONSERTO REPARO OU INDUSTRIALIZACAO;DO IMPOSTO CORRESPONDENTE AOS SERVICOS PRESTADOS;ENCOMENDA FEITA POR CONTRIBUINTE SALVO USO E CONSUMO;ANEXO 3 ART 7 X
GERAL;MERCADORIAS MAQUINAS APARELHOS E EQUIPAMENTOS DESTINADOS A EMPRESA BENEFICIADA PELO REPORTO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;PARA UTILIZACAO EXCLUSIVA EM PORTO LOCALIZADO EM TERRITORIO CATARINENSE;ANEXO 3 ART 7 XVII
GERAL;MERCADORIA DE ESTABELECIMENTO DE COOPERATIVA COM DESTINO A EMPRESA COMERCIAL EXPORTADORA;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;RELATIVAMENTE AS OPERACOES NAO ALCANCADAS PELO BENEFICIO DE ISENCAO PARA EXPORTACAO;ANEXO 3 ART 7 XIX
2204;VINHO;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;PROMOVIDA PELO ESTABELECIMENTO INDUSTRIAL QUE O TENHA PRODUZIDO COM DESTINO A OUTRO ESTABELECIMENTO INDUSTRIAL PRODUTOR DE VINHO;ANEXO 3 ART 7 XX
7010;GARRAFAS DE VIDRO VAZIAS;PARA A ETAPA SEGUINTE DE CIRCULACAO NA SAIDA;COM DESTINO A ESTABELECIMENTO INDUSTRIAL PARA SEREM UTILIZADAS COMO EMBALAGEM DE PRODUTOS;ANEXO 3 ART 7 XXVII
0203;CARNES E MIUDEZAS COMESTIVEIS DE SUINOS FRESCAS REFRIGERADAS CONGELADAS OU TEMPERADAS;PARA A ETAPA SEGUINTE DE CIRCULACAO NAS SAIDAS INTERNAS;PRODUZIDOS E ABATIDOS NESTE ESTADO VIGENCIA ATE 31 DE DEZEMBRO DE 2006;ANEXO 3 ART 9
GERAL;MERCADORIA IMPORTADA DO EXTERIOR SEM SIMILAR PRODUZIDO NO PAIS;PARA A ETAPA SEGUINTE DE CIRCULACAO NA ENTRADA;IMPORTACAO POR MEIO DE PORTOS OU AEROPORTOS DE SC DESTINADA A COMERCIALIZACAO OU INDUSTRIALIZACAO;ANEXO 3 ART 10
3900;PLASTICO E SUAS OBRAS DESTINADOS A CONSTRUCAO CIVIL;PARCIAL DE 29,411 POR CENTO NA ALIQ 17 POR CENTO E 52 POR CENTO NA ALIQ 25 POR CENTO DO IMPOSTO DEVIDO;SAIDA DE ESTABELECIMENTO INDUSTRIAL;ANEXO 3 ART 10-B I
2204;VINHO;PARCIAL DE 29,411 POR CENTO NA ALIQ 17 POR CENTO E 52 POR CENTO NA ALIQ 25 POR CENTO DO IMPOSTO DEVIDO;PROMOVIDA POR ESTABELECIMENTO INDUSTRIAL PRODUTOR DE VINHO;ANEXO 3 ART 10-B VI
GERAL;MERCADORIAS PROMOVIDAS POR CENTRO DE DISTRIBUICAO;PARCIAL DE 29,411 POR CENTO NA ALIQ 17 POR CENTO E 52 POR CENTO NA ALIQ 25 POR CENTO DO IMPOSTO DEVIDO;SAIDA DO CENTRO DE DISTRIBUICAO;ANEXO 3 ART 10-B VII
GERAL;BENS PARA ATIVO PERMANENTE DE CONCESSIONARIA DE SERVICO PUBLICO DE TRANSMISSAO DE ENERGIA ELETRICA;DO IMPOSTO RELATIVO AO DIFERENCIAL DE ALIQUOTAS NAS ENTRADAS INTERESTADUAIS;NA;ANEXO 3 ART 10-C
GERAL;MAQUINAS APARELHOS E EQUIPAMENTOS SEM SIMILAR NACIONAL;DO IMPOSTO INCIDENTE NA OPERACAO DE IMPORTACAO;DESTINADOS A INTEGRAR O ATIVO PERMANENTE DE EMPRESA INDUSTRIAL OU AGROINDUSTRIAL IMPORTACAO POR PORTOS OU AEROPORTOS DE SC;ANEXO 3 ART 10-D
0300;PESCADOS PROCESSADOS;PARCIAL DE 41,17 POR CENTO NA ALIQ 17 POR CENTO 16,66 POR CENTO NA ALIQ 12 POR CENTO E 60 POR CENTO NA ALIQ 25 POR CENTO;SAIDAS DE ESTABELECIMENTO INDUSTRIAL COM BENEFICIO DO ART 21 § 4 I B DO ANEXO 2;ANEXO 3 ART 10-F
GERAL;MERCADORIAS DESTINADAS A CONTRIBUINTE COM TTD DO DECRETO 105/2007 ART 10;TOTAL DO IMPOSTO INCIDENTE NAS SAIDAS INTERNAS;NA;ANEXO 3 ART 10-G
GERAL;MATERIAS-PRIMAS MATERIAL SECUNDARIO EMBALAGENS ENERGIA ELETRICA E GAS NATURAL;TOTAL OU PARCIAL DO IMPOSTO DEVIDO NAS SAIDAS;DESTINO A ESTABELECIMENTOS INDUSTRIAIS COM CREDITOS ACUMULADOS DE EXPORTACAO MEDIANTE REGIME ESPECIAL;ANEXO 3 ART 10-H
GERAL;MERCADORIA IMPORTADA PARA COMERCIALIZACAO;DO PAGAMENTO DO IMPOSTO DEVIDO NO DESEMBARACO ADUANEIRO PARA A ETAPA SEGUINTE A DA ENTRADA;DESEMBARACO REALIZADO POR INTERMEDIO DE PORTOS AEROPORTOS OU PONTOS DE FRONTEIRA ALFANDEGADOS SITUADOS EM SC MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 246 I
GERAL;MERCADORIA IMPORTADA PARA COMERCIALIZACAO SAIDA INTERNA;PARCIAL DO IMPOSTO NA SAIDA INTERNA PARA ESTABELECIMENTO INDUSTRIAL;DESTINADO A INDUSTRIALIZACAO PELO DESTINATARIO;ANEXO 2 ART 246 § 23
7200;ACO IMPORTADO SAIDA INTERNA;PARCIAL DO IMPOSTO NA SAIDA INTERNA PARA ESTABELECIMENTO INDUSTRIAL;DESTINADO A PROCESSO INDUSTRIAL DE PURIFICACAO CONCENTRACAO ETC;ANEXO 2 ART 246 § 24
7600;ALUMINIO IMPORTADO SAIDA INTERNA;PARCIAL DO IMPOSTO NA SAIDA INTERNA PARA ESTABELECIMENTO INDUSTRIAL;DESTINADO A PROCESSO INDUSTRIAL DE PURIFICACAO CONCENTRACAO ETC;ANEXO 2 ART 246 § 24
7400;COBRE IMPORTADO SAIDA INTERNA;PARCIAL DO IMPOSTO NA SAIDA INTERNA PARA ESTABELECIMENTO INDUSTRIAL;DESTINADO A PROCESSO INDUSTRIAL DE PURIFICACAO CONCENTRACAO ETC;ANEXO 2 ART 246 § 24
2704;COQUE IMPORTADO SAIDA INTERNA;PARCIAL DO IMPOSTO NA SAIDA INTERNA PARA ESTABELECIMENTO INDUSTRIAL;DESTINADO A PROCESSO INDUSTRIAL DE PURIFICACAO CONCENTRACAO ETC;ANEXO 2 ART 246 § 24
7106;PRATA IMPORTADA SAIDA INTERNA;PARCIAL DO IMPOSTO NA SAIDA INTERNA PARA ESTABELECIMENTO INDUSTRIAL;DESTINADO A PROCESSO INDUSTRIAL DE PURIFICACAO CONCENTRACAO ETC;ANEXO 2 ART 246 § 24
GERAL;BENS PARA ATIVO IMOBILIZADO INDUSTRIA DE ESTRUTURAS METALICAS;DO PAGAMENTO DO IMPOSTO NO DESEMBARACO ADUANEIRO DE BENS IMPORTADOS DIRETAMENTE DO EXTERIOR;SEM SIMILAR PRODUZIDO EM SC MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 250 I A
GERAL;BENS E MERCADORIAS PARA ATIVO IMOBILIZADO INDUSTRIA SIDERURGICA;DO PAGAMENTO DO IMPOSTO NA AQUISICAO INTERNA E DIFAL NA AQUISICAO INTERESTADUAL;MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 256 I
GERAL;BENS PARA ATIVO IMOBILIZADO INDUSTRIA DE LAMINAS DE MADEIRA COMPOSTA;DO PAGAMENTO DO IMPOSTO NO DESEMBARACO ADUANEIRO DE BENS IMPORTADOS DIRETAMENTE DO EXTERIOR;SEM SIMILAR PRODUZIDO EM SC MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 258 I A
1507;OLEO DEGOMADO;DO PAGAMENTO DO IMPOSTO INCIDENTE NA ENTRADA;DESTINADO A PRODUCAO DE BIODIESEL PELO PROPRIO ESTABELECIMENTO BENEFICIARIO MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 259 I
GERAL;BENS PARA ATIVO IMOBILIZADO INDUSTRIA DE EMBALAGENS;DO PAGAMENTO DO IMPOSTO NO DESEMBARACO ADUANEIRO DE BENS IMPORTADOS DIRETAMENTE DO EXTERIOR;SEM SIMILAR PRODUZIDO EM SC MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 262 I A
GERAL;SAIDA INTERNA DE PRODUTOR RURAL COM DESTINO A CONAB/PAA;DO IMPOSTO NA SAIDA;O IMPOSTO DEVIDO SERA RECOLHIDO PELA CONAB/PAA COMO SUBSTITUTA TRIBUTARIA;ANEXO 6 ART 248
8537;SUBESTACAO ISOLADA A GAS SF6;ISENTA A ENTRADA DECORRENTE DA IMPORTACAO E A SUBSEQUENTE SAIDA INTERNA;DESTINADA A USINA HIDRELETRICA DE MACHADINHO SEM SIMILAR PRODUZIDO NO PAIS;ANEXO 2 ART 86
GERAL;MERCADORIA IMPORTADA PARA COMERCIALIZACAO POR ESTABELECIMENTO IMPORTADOR;DO PAGAMENTO DO IMPOSTO DEVIDO NO DESEMBARACO ADUANEIRO PARA A ETAPA SEGUINTE A DA ENTRADA;MEDIANTE REGIME ESPECIAL CONFORME LEI 17763/19 ANEXO II ART 1;ANEXO 2 ART 246 I
GERAL;BENS E MERCADORIAS PRODUZIDAS EM SC PARA ATIVO IMOBILIZADO INDUSTRIA DE ESTRUTURAS METALICAS;DO PAGAMENTO DO IMPOSTO INCIDENTE SOBRE AS OPERACOES DE AQUISICAO;MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 250 I B
GERAL;BENS E MERCADORIAS DE OUTROS ESTADOS PARA ATIVO IMOBILIZADO INDUSTRIA DE ESTRUTURAS METALICAS;DO PAGAMENTO DO IMPOSTO RELATIVO AO DIFERENCIAL DE ALIQUOTA;MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 250 I C
GERAL;BENS E MERCADORIAS PRODUZIDAS EM SC PARA ATIVO IMOBILIZADO INDUSTRIA DE LAMINAS DE MADEIRA COMPOSTA;DO PAGAMENTO DO IMPOSTO INCIDENTE SOBRE AS OPERACOES DE AQUISICAO;MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 258 I B
GERAL;BENS E MERCADORIAS DE OUTROS ESTADOS PARA ATIVO IMOBILIZADO INDUSTRIA DE LAMINAS DE MADEIRA COMPOSTA;DO PAGAMENTO DO IMPOSTO RELATIVO AO DIFERENCIAL DE ALIQUOTA;MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 258 I C
GERAL;BENS E MERCADORIAS PRODUZIDAS EM SC PARA ATIVO IMOBILIZADO INDUSTRIA DE EMBALAGENS;DO PAGAMENTO DO IMPOSTO RELATIVO A AQUISICAO;MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 262 I B
GERAL;BENS E MERCADORIAS DE OUTROS ESTADOS PARA ATIVO IMOBILIZADO INDUSTRIA DE EMBALAGENS;DO PAGAMENTO DO IMPOSTO RELATIVO AO DIFERENCIAL DE ALIQUOTA;MEDIANTE REGIME ESPECIAL;ANEXO 2 ART 262 I C
GERAL;ENERGIA ELETRICA ADQUIRIDA EM AMBIENTE DE CONTRATACAO LIVRE;DO IMPOSTO INCIDENTE NAS SUCESSIVAS OPERACOES INTERNAS E INTERESTADUAIS;RESPONSABILIDADE PELO PAGAMENTO ATRIBUIDA AO CONSUMIDOR LIVRE;ANEXO 3 ART 245

ALÍQUOTA:
NCM;DESCRIÇÃO;ALÍQUOTA ICMS;BASE LEGAL
0101;CAVALOS ASININOS E MUARES VIVOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0102;ANIMAIS VIVOS DA ESPECIE BOVINA;12;RICMS SC Art 26 III e Anexo 1 Secao III
0103;ANIMAIS VIVOS DA ESPECIE SUINA;12;RICMS SC Art 26 III e Anexo 1 Secao III
0104;ANIMAIS VIVOS DAS ESPECIES OVINA E CAPRINA;12;RICMS SC Art 26 III e Anexo 1 Secao III
0105;AVES DA ESPECIE GALLUS DOMESTICUS PATOS GANSOS PERUS PERUAS E GALINHAS-D'ANGOLA PINTADAS DAS ESPECIES DOMESTICAS VIVOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0106;OUTROS ANIMAIS VIVOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0201;CARNES DE ANIMAIS DA ESPECIE BOVINA FRESCAS OU REFRIGERADAS;12;RICMS SC Art 26 III e Anexo 1 Secao II
0202;CARNES DE ANIMAIS DA ESPECIE BOVINA CONGELADAS;12;RICMS SC Art 26 III e Anexo 1 Secao II
0203;CARNES DE ANIMAIS DA ESPECIE SUINA FRESCAS REFRIGERADAS OU CONGELADAS;12;RICMS SC Art 26 III e Anexo 1 Secao II
0204;CARNES DE ANIMAIS DAS ESPECIES OVINA OU CAPRINA FRESCAS REFRIGERADAS OU CONGELADAS;12;RICMS SC Art 26 III e Anexo 1 Secao II
0206;MIUDEZAS COMESTIVEIS DE ANIMAIS DAS ESPECIES BOVINA SUINA OVINA CAPRINA CAVALAR ASININA E MUAR FRESCAS REFRIGERADAS OU CONGELADAS;12;RICMS SC Art 26 III e Anexo 1 Secao II
0207;CARNES E MIUDEZAS COMESTIVEIS DE AVES DA POSICAO 0105 FRESCAS REFRIGERADAS OU CONGELADAS;12;RICMS SC Art 26 III e Anexo 1 Secao II
0210;CARNES E MIUDEZAS COMESTIVEIS SALGADAS OU EM SALMOURA SECAS OU DEFUMADAS FARINHAS E POS COMESTIVEIS DE CARNES OU DE MIUDEZAS;12;RICMS SC Art 26 III e Anexo 1 Secao II
0301;PEIXES VIVOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0302;PEIXES FRESCOS OU REFRIGERADOS EXCETO OS FILES DE PEIXES E OUTRA CARNE DE PEIXES DA POSICAO 0304;12;RICMS SC Art 26 III e Anexo 1 Secao III
0303;PEIXES CONGELADOS EXCETO OS FILES DE PEIXES E OUTRA CARNE DE PEIXES DA POSICAO 0304;12;RICMS SC Art 26 III e Anexo 1 Secao III
0304;FILES DE PEIXES E OUTRA CARNE DE PEIXES MESMO PICADA FRESCOS REFRIGERADOS OU CONGELADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0305;PEIXES SECOS SALGADOS OU EM SALMOURA PEIXES DEFUMADOS MESMO COZIDOS ANTES OU DURANTE A DEFUMACAO;12;RICMS SC Art 26 III e Anexo 1 Secao III
0306;CRUSTACEOS MESMO COM CASCA VIVOS FRESCOS REFRIGERADOS CONGELADOS SECOS SALGADOS OU EM SALMOURA;12;RICMS SC Art 26 III e Anexo 1 Secao III
0307;MOLUSCOS COM OU SEM CONCHA VIVOS FRESCOS REFRIGERADOS CONGELADOS SECOS SALGADOS OU EM SALMOURA;12;RICMS SC Art 26 III e Anexo 1 Secao III
0401;LEITE E CREME DE LEITE NATA NAO CONCENTRADOS NEM ADICIONADOS DE ACUCAR OU DE OUTROS EDULCORANTES;12;RICMS SC Art 26 III e Anexo 1 Secao II
0402;LEITE E CREME DE LEITE NATA CONCENTRADOS OU ADICIONADOS DE ACUCAR OU DE OUTROS EDULCORANTES;12;RICMS SC Art 26 III e Anexo 1 Secao II
0405;MANTEIGA E OUTRAS MATERIAS GORDAS PROVENIENTES DO LEITE;12;RICMS SC Art 26 III e Anexo 1 Secao II
0406;QUEIJOS E REQUEIJAO;12;RICMS SC Art 26 III e Anexo 1 Secao II
0407;OVOS DE AVES COM CASCA FRESCOS CONSERVADOS OU COZIDOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0409;MEL NATURAL;12;RICMS SC Art 26 III e Anexo 1 Secao II
0701;BATATAS FRESCAS OU REFRIGERADAS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0702;TOMATES FRESCOS OU REFRIGERADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0703;CEBOLAS ALHOS ALHOS-POROS E OUTROS PRODUTOS HORTICOLAS ALIACEOS FRESCOS OU REFRIGERADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0704;COUVES COUVE-FLOR REPOLHO OU COUVE FRISADA COUVE-RABANO E PRODUTOS COMESTIVEIS SEMELHANTES DO GENERO BRASSICA FRESCOS OU REFRIGERADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0705;ALFACE E CHICORIA COMPREENDIDAS A ESCAROLA E A ENDIVIA FRESCAS OU REFRIGERADAS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0706;CENOURAS NABOS BETERRABAS PARA SALADA CERCEFI AIPO-RABANO RABANETES E RAIZES COMESTIVEIS SEMELHANTES FRESCOS OU REFRIGERADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0707;PEPINOS E PEPININHOS CORNICHONS FRESCOS OU REFRIGERADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0708;LEGUMES DE VAGEM MESMO COM VAGEM FRESCOS OU REFRIGERADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0709;OUTROS PRODUTOS HORTICOLAS FRESCOS OU REFRIGERADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0713;LEGUMES DE VAGEM SECOS EM GRAOS MESMO COM PELE OU PARTIDOS;12;RICMS SC Art 26 III e Anexo 1 Secao II
0714;RAIZES DE MANDIOCA DE ARARUTA E DE SALEPO TOPINAMBOS BATATAS-DOCES E RAIZES E TUBERCULOS SEMELHANTES COM ELEVADO TEOR DE FECULA OU DE INULINA FRESCOS REFRIGERADOS CONGELADOS OU SECOS MESMO CORTADOS EM PEDACOS OU EM PELLETS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0801;COCOS CASTANHA-DO-BRASIL E CASTANHA-DE-CAJU FRESCOS OU SECOS MESMO COM CASCA OU PELADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0802;OUTRA FRUTA DE CASCA RIJA FRESCA OU SECA MESMO COM CASCA OU PELADA;12;RICMS SC Art 26 III e Anexo 1 Secao III
0803;BANANAS INCLUINDO AS BANANAS-DA-TERRA FRESCAS OU SECAS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0804;TAMARAS FIGOS ABACAXIS ABACATES GOIABAS MANGAS E MANGOSTOES FRESCOS OU SECOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0805;CITROS FRESCOS OU SECOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0806;UVAS FRESCAS OU SECAS PASSAS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0807;MELOES MELANCIAS E MAMOES FRESCOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0808;MACAS PERAS E MARMELOS FRESCOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0809;DAMASCOS CEREJAS PESSEGOS INCLUINDO AS NECTARINAS AMEIXAS E ABRUNHOS FRESCOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0810;OUTRA FRUTA FRESCA;12;RICMS SC Art 26 III e Anexo 1 Secao III
0901;CAFE MESMO TORRADO OU DESCAFEINADO CASCAS E PELICULAS DE CAFE SUCEDANEOS DO CAFE QUE CONTENHAM CAFE EM QUALQUER PROPORCAO;12;RICMS SC Art 26 III e Anexo 1 Secao II
0902;CHA MESMO AROMATIZADO;12;RICMS SC Art 26 III e Anexo 1 Secao III
0903;MATE;12;RICMS SC Art 26 III e Anexo 1 Secao II
0904;PIMENTA DO GENERO PIPER PIMENTOES E PIMENTAS DO GENERO CAPSICUM OU DO GENERO PIMENTA SECOS OU TRITURADOS OU EM PO;12;RICMS SC Art 26 III e Anexo 1 Secao III
0905;BAUNILHA;12;RICMS SC Art 26 III e Anexo 1 Secao III
0906;CANELA E FLORES DE CANELEIRA;12;RICMS SC Art 26 III e Anexo 1 Secao III
0907;CRAVO-DA-INDIA FRUTOS FLORES E PEDUNCULOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0908;NOZ-MOSCADA MACIS AMOMOS E CARDAMOMOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
0909;SEMENTES DE ANIS BADIANA FUNCHO COENTRO COMINHO OU DE ALCARAVIA BAGAS DE ZIMBRO;12;RICMS SC Art 26 III e Anexo 1 Secao III
0910;GENGIBRE ACAFRAO-DA-TERRA CURCUMA TOMILHO LOURO CARRIL E OUTRAS ESPECIARIAS;12;RICMS SC Art 26 III e Anexo 1 Secao III
1001;TRIGO E MISTURA DE TRIGO COM CENTEIO METEIL;12;RICMS SC Art 26 III e Anexo 1 Secao III
1002;CENTEIO;12;RICMS SC Art 26 III e Anexo 1 Secao III
1003;CEVADA;12;RICMS SC Art 26 III e Anexo 1 Secao III
1004;AVEIA;12;RICMS SC Art 26 III e Anexo 1 Secao III
1005;MILHO;12;RICMS SC Art 26 III e Anexo 1 Secao III
1006;ARROZ;12;RICMS SC Art 26 III e Anexo 1 Secao II
1007;SORGO DE GRAO;12;RICMS SC Art 26 III e Anexo 1 Secao III
1008;TRIGO SARRACENO PAINCO E ALPISTE OUTROS CEREAIS;12;RICMS SC Art 26 III e Anexo 1 Secao III
1101;FARINHAS DE TRIGO OU DE MISTURA DE TRIGO COM CENTEIL METEIL;12;RICMS SC Art 26 III e Anexo 1 Secao II
1102;FARINHAS DE CEREAIS EXCETO DE TRIGO OU DE MISTURA DE TRIGO COM CENTEIO METEIL;12;RICMS SC Art 26 III e Anexo 1 Secao II
1105;FARINHA SEMOLA PO FLOCOS GRANULOS E PELLETS DE BATATA;12;RICMS SC Art 26 III e Anexo 1 Secao II
1201;SOJA MESMO TRITURADA;12;RICMS SC Art 26 III e Anexo 1 Secao III
1202;AMENDOINS NAO TORRADOS NEM DE OUTRO MODO COZIDOS MESMO COM CASCA OU TRITURADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
1203;COPRA;12;RICMS SC Art 26 III e Anexo 1 Secao III
1204;LINHACA SEMENTE DE LINHO MESMO TRITURADA;12;RICMS SC Art 26 III e Anexo 1 Secao III
1205;SEMENTES DE NABO SILVESTRE OU DE COLZA MESMO TRITURADAS;12;RICMS SC Art 26 III e Anexo 1 Secao III
1206;SEMENTES DE GIRASSOL MESMO TRITURADAS;12;RICMS SC Art 26 III e Anexo 1 Secao III
1207;OUTRAS SEMENTES E FRUTOS OLEAGINOSOS MESMO TRITURADOS;12;RICMS SC Art 26 III e Anexo 1 Secao III
1212;ALFARROBA ALGAS BETERRABA SACARINA E CANA-DE-ACUCAR FRESCAS REFRIGERADAS CONGELADAS OU SECAS MESMO EM PO;12;RICMS SC Art 26 III e Anexo 1 Secao III
1501;GORDURAS DE PORCO INCLUINDO A BANHA E OUTRAS GORDURAS DE AVES PRENSADAS OU FUNDIDAS MESMO EMULSIFICADAS;12;RICMS SC Art 26 III e Anexo 1 Secao II
1507;OLEO DE SOJA E RESPECTIVAS FRACOES MESMO REFINADOS MAS NAO QUIMICAMENTE MODIFICADOS;12;RICMS SC Art 26 III e Anexo 1 Secao II
1515;OUTRAS GORDURAS E OLEOS VEGETAIS FIXOS INCLUINDO O OLEO DE JOJOBA E RESPECTIVAS FRACOES MESMO REFINADOS MAS NAO QUIMICAMENTE MODIFICADOS;12;RICMS SC Art 26 III e Anexo 1 Secao II
1517;MARGARINA MISTURAS OU PREPARACOES ALIMENTICIAS DE GORDURAS OU DE OLEOS ANIMAIS OU VEGETAIS OU DE FRACOES DAS DIFERENTES GORDURAS OU OLEOS DESTE CAPITULO EXCETO AS GORDURAS E OLEOS ALIMENTICIOS E RESPECTIVAS FRACOES DA POSICAO 1516;12;RICMS SC Art 26 III e Anexo 1 Secao II
1604;PREPARACOES E CONSERVAS DE PEIXES CAVIAR E SEUS SUCEDANEOS PREPARADOS A PARTIR DE OVAS DE PEIXE;12;RICMS SC Art 26 III e Anexo 1 Secao II
1701;ACUCARES DE CANA OU DE BETERRABA E SACAROSE QUIMICAMENTE PURA NO ESTADO SOLIDO;12;RICMS SC Art 26 III e Anexo 1 Secao II
1901;EXTRATOS DE MALTE PREPARACOES ALIMENTICIAS DE FARINHAS GRUMOS SEMOLAS AMIDOS FECULAS OU DE EXTRATOS DE MALTE;12;RICMS SC Art 26 III e Anexo 1 Secao II
1902;MASSAS ALIMENTICIAS MESMO COZIDAS OU RECHEADAS DE CARNE OU DE OUTRAS SUBSTANCIAS OU PREPARADAS DE OUTRO MODO;7;RICMS SC Anexo 2 Art 11-A III
1905;PRODUTOS DE PADARIA PASTELARIA OU DA INDUSTRIA DE BOLACHAS E BISCOITOS MESMO ADICIONADOS DE CACAU;7;RICMS SC Anexo 2 Art 11-A IV
2106;PREPARACOES ALIMENTICIAS NAO ESPECIFICADAS NEM COMPREENDIDAS NOUTRAS POSICOES;5;RICMS SC Anexo 2 Art 15 XL
2203;CERVEJAS DE MALTE;25;RICMS SC Art 26 I e Anexo 1 Secao I
2204;VINHOS DE UVAS FRESCAS INCLUINDO OS VINHOS ENRIQUECIDOS COM ALCOOL MOSTOS DE UVAS;25;RICMS SC Art 26 I e Anexo 1 Secao I
2205;VERMUTES E OUTROS VINHOS DE UVAS FRESCAS AROMATIZADOS POR PLANTAS OU SUBSTANCIAS AROMATICAS;25;RICMS SC Art 26 I e Anexo 1 Secao I
2206;OUTRAS BEBIDAS FERMENTADAS MISTURAS DE BEBIDAS FERMENTADAS E MISTURAS DE BEBIDAS FERMENTADAS COM BEBIDAS NAO ALCOOLICAS;25;RICMS SC Art 26 I e Anexo 1 Secao I
2208;ALCOOL ETILICO NAO DESNATURADO COM UM TEOR ALCOOLICO EM VOLUME INFERIOR A 80% VOL AGUARDENTES LICORES E OUTRAS BEBIDAS ESPIRITUOSAS;25;RICMS SC Art 26 I e Anexo 1 Secao I
2209;VINAGRES E SEUS SUCEDANEOS OBTIDOS A PARTIR DO ACIDO ACETICO PARA USOS ALIMENTARES;12;RICMS SC Art 26 III e Anexo 1 Secao II
2401;TABACO NAO MANUFATURADO DESPERDICIOS DE TABACO;12;RICMS SC Art 26 III e Anexo 1 Secao III
2402;CHARUTOS CIGARRILHAS E CIGARROS DE TABACO OU DOS SEUS SUCEDANEOS;25;RICMS SC Art 26 I e Anexo 1 Secao I
2403;OUTROS PRODUTOS DE TABACO E SEUS SUCEDANEOS MANUFATURADOS TABACO HOMOGENEIZADO OU RECONSTITUIDO EXTRATOS E MOLHOS DE TABACO;25;RICMS SC Art 26 I e Anexo 1 Secao I
2501;SAL INCLUIDOS O SAL DE MESA E O SAL DENATURADO E CLORETO DE SODIO PURO MESMO EM SOLUCAO AQUOSA OU ADICIONADO DE AGENTES ANTIAGLOMERANTES OU DE AGENTES QUE ASSEGUREM UMA BOA FLUIDEZ;12;RICMS SC Art 26 III e Anexo 1 Secao II
2704;COQUES E SEMICOQUES DE HULHA DE LINHITA OU DE TURFA MESMO AGLOMERADOS CARVAO DE RETORTA;12;RICMS SC Art 26 III f
2710;OLEOS DE PETROLEO OU DE MINERAIS BETUMINOSOS EXCETO OLEOS BRUTOS PREPARACOES CONTENDO EM PESO 70% OU MAIS DE OLEOS DE PETROLEO OU DE MINERAIS BETUMINOSOS;12;RICMS SC Art 26 III f
3303;PERFUMES E AGUAS-DE-COLONIA;25;RICMS SC Art 26 I e Anexo 1 Secao I
3304;PRODUTOS DE BELEZA OU DE MAQUIAGEM PREPARADOS E PREPARACOES PARA CONSERVACAO OU CUIDADOS DA PELE;25;RICMS SC Art 26 I e Anexo 1 Secao I
3305;PREPARACOES CAPILARES;25;RICMS SC Art 26 I e Anexo 1 Secao I
3307;PREPARACOES PARA BARBEAR DESODORANTES CORPORAIS PREPARACOES PARA BANHOS;25;RICMS SC Art 26 I e Anexo 1 Secao I
3924;SERVICOS DE MESA E OUTROS ARTIGOS DE USO DOMESTICO DE HIGIENE OU DE TOUCADOR DE PLASTICO;3;RICMS SC Anexo 2 Art 15 XLVIII
4301;PELES COM PELO EM BRUTO;25;RICMS SC Art 26 I e Anexo 1 Secao I
4302;PELES COM PELO CURTIDAS OU ACABADAS;25;RICMS SC Art 26 I e Anexo 1 Secao I
4303;VESTUARIO SEUS ACESSORIOS E OUTROS ARTIGOS DE PELES COM PELO;25;RICMS SC Art 26 I e Anexo 1 Secao I
4304;PELES COM PELO ARTIFICIAIS E SUAS OBRAS;25;RICMS SC Art 26 I e Anexo 1 Secao I
4401;LENHA EM TORAS EM LASCAS OU EM PARTES MADEIRA EM ESTILHAS OU EM PARTICULAS SERRAGEM DESPERDICIOS E RESIDUOS DE MADEIRA;12;RICMS SC Art 26 III e Anexo 1 Secao III
4403;MADEIRA EM BRUTO MESMO DESCASCADA ESQUADRIADA OU NAO;12;RICMS SC Art 26 III e Anexo 1 Secao III
5001;CASULOS DE BICHO-DA-SEDA PROPRIOS PARA DOBAR;12;RICMS SC Art 26 III e Anexo 1 Secao III
6810;OBRAS DE CIMENTO DE CONCRETO OU DE PEDRA ARTIFICIAL MESMO ARMADAS;12;RICMS SC Art 26 III h
6907;LADRILHOS E PLACAS LAJES PARA PAVIMENTACAO OU REVESTIMENTO DE CERAMICA;12;RICMS SC Art 26 III g
6908;LADRILHOS E PLACAS LAJES PARA PAVIMENTACAO OU REVESTIMENTO DE CERAMICA VIDRADOS OU ESMALTADOS;12;RICMS SC Art 26 III g
6910;PIAS LAVATORIOS COLUNAS PARA LAVATORIOS BANHEIRAS BIDES SANITARIOS CAIXAS DE DESCARGA MICTORIOS E APARELHOS FIXOS SEMELHANTES PARA USOS SANITARIOS DE CERAMICA;12;RICMS SC Art 26 III g
6911;LOUCA OUTROS ARTIGOS DE USO DOMESTICO E ARTIGOS DE HIGIENE OU DE TOUCADOR DE PORCELANA;8.5;RICMS SC Anexo 2 Art 8 VIII
7013;OBJETOS DE VIDRO PARA SERVICO DE MESA COZINHA TOUCADOR ESCRITORIO ORNAMENTACAO DE INTERIORES OU USOS SEMELHANTES;8.5;RICMS SC Anexo 2 Art 8 VIII
7326;OUTRAS OBRAS DE FERRO OU ACO;12;RICMS SC Anexo 2 Art 7 XXI
8407;MOTORES DE PISTAO ALTERNATIVO OU ROTATIVO DE IGNICAO POR CENTELHA FAISCA;12;RICMS SC Anexo 2 Art 12-C
8408;MOTORES DE PISTAO DE IGNICAO POR COMPRESSAO DIESEL OU SEMIDIESEL;12;RICMS SC Anexo 2 Art 12-C
8409;PARTES RECONHECIVEIS COMO EXCLUSIVA OU PRINCIPALMENTE DESTINADAS AOS MOTORES DAS POSICOES 8407 OU 8408;12;RICMS SC Anexo 2 Art 12-C
8414;COIFAS E DEPURADORES DOMESTICOS;2.5;RICMS SC Anexo 2 Art 15 L
8415;MAQUINAS E APARELHOS DE AR-CONDICIONADO CONTENDO UM VENTILADOR MOTORIZADO E DISPOSITIVOS PROPRIOS PARA MODIFICAR A TEMPERATURA E A UMIDADE;2.5;RICMS SC Anexo 2 Art 15 L
8418;REFRIGERADORES CONGELADORES FREEZERS E OUTROS MATERIAIS MAQUINAS E APARELHOS PARA A PRODUCAO DE FRIO;2.5;RICMS SC Anexo 2 Art 15 L
8419;MAQUINAS APARELHOS E DISPOSITIVOS MESMO DE AQUECIMENTO ELETRICO EXCETO OS DA POSICAO 8514 PARA TRATAMENTO DE MATERIAS POR MEIO DE OPERACOES QUE ENVOLVAM MUDANCA DE TEMPERATURA;8.8;RICMS SC Anexo 2 Art 9 I
8420;CALANDRAS E LAMINADORES EXCETO OS DESTINADOS AO TRATAMENTO DE METAIS OU VIDRO E SEUS CILINDROS;8.8;RICMS SC Anexo 2 Art 9 I
8421;CENTRIFUGADORES INCLUINDO OS SECADORES CENTRIFUGOS APARELHOS PARA FILTRAR OU DEPURAR LIQUIDOS OU GASES;8.8;RICMS SC Anexo 2 Art 9 I
8422;MAQUINAS DE LAVAR LOUCA MAQUINAS E APARELHOS PARA LIMPAR OU SECAR GARRAFAS OU OUTROS RECIPIENTES;2.5;RICMS SC Anexo 2 Art 15 L
8424;MAQUINAS E APARELHOS PARA PULVERIZAR OU DISPERSAR;2.5;RICMS SC Anexo 2 Art 15 L
8427;EMPILHADEIRAS OUTROS VEICULOS PARA MOVIMENTACAO DE CARGA E SEMELHANTES EQUIPADOS COM DISPOSITIVOS DE ELEVACAO;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8428;OUTRAS MAQUINAS E APARELHOS DE ELEVACAO DE CARGA DE DESCARGA OU DE MOVIMENTACAO;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8429;ESCAVADORAS DE LAGARTAS ESCAVADORAS NIVELADORAS RASPO-TRANSPORTADORAS SCRAPERS MOTONIVELADORAS ROLOS COMPRESSORES E OUTROS VEICULOS SEMELHANTES AUTOPROPULSORES;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8434;MAQUINAS DE ORDENHAR E MAQUINAS E APARELHOS PARA A INDUSTRIA DE LATICINIOS;11.45;RICMS SC Anexo 2 Art 9 II
8435;PRENSAS ESMAGADORES E MAQUINAS E APARELHOS SEMELHANTES PARA FABRICACAO DE VINHO SIDRA SUCOS DE FRUTA OU BEBIDAS SEMELHANTES;11.45;RICMS SC Anexo 2 Art 9 II
8443;MAQUINAS E APARELHOS DE IMPRESSAO POR MEIO DE PLACAS CILINDROS E OUTROS ELEMENTOS DE IMPRESSAO DA POSICAO 8442;7;RICMS SC Anexo 2 Art 7 VII
8517;APARELHOS TELEFONICOS INCLUINDO OS TELEFONES PARA REDES CELULARES E PARA OUTRAS REDES SEM FIO;3;RICMS SC Anexo 2 Art 15 XXXI
8701;TRATORES EXCETO OS CARROS-TRATORES DA POSICAO 8709;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8702;VEICULOS AUTOMOVEIS PARA TRANSPORTE DE DEZ PESSOAS OU MAIS INCLUINDO O MOTORISTA;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8703;AUTOMOVEIS DE PASSAGEIROS E OUTROS VEICULOS AUTOMOVEIS PRINCIPALMENTE CONCEBIDOS PARA TRANSPORTE DE PESSOAS;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8704;VEICULOS AUTOMOVEIS PARA TRANSPORTE DE MERCADORIAS;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8706;CHASSIS COM MOTOR PARA VEICULOS AUTOMOVEIS DAS POSICOES 8701 A 8705;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8707;CARROCARIA PARA OS VEICULOS AUTOMOVEIS DAS POSICOES 8701 A 8705 INCLUINDO AS CABINAS;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8711;MOTOCICLETAS INCLUIDOS OS CICLOMOTORES E OUTROS CICLOS EQUIPADOS COM MOTOR AUXILIAR MESMO COM CARRO LATERAL;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8716;REBOQUES E SEMIRREBOQUES PARA QUAISQUER VEICULOS OUTROS VEICULOS NAO AUTOPROPULSORES SUAS PARTES;12;RICMS SC Art 26 III e Anexo 1 Secao IV
8801;BALOES E DIRIGIVEIS PLANADORES ASAS VOADORAS E OUTROS VEICULOS AEREOS NAO CONCEBIDOS PARA PROPULSAO COM MOTOR;25;RICMS SC Art 26 I e Anexo 1 Secao I
8903;IATES E OUTROS BARCOS E EMBARCACOES DE RECREIO OU DE ESPORTE BARCOS A REMOS E CANOAS;12;RICMS SC Art 26 III e Anexo 1 Secao IV
9301;ARMAS DE GUERRA EXCETO REVOLVERES PISTOLAS E ARMAS BRANCAS;25;RICMS SC Art 26 I e Anexo 1 Secao I
9302;REVOLVERES E PISTOLAS EXCETO OS DAS POSICOES 9303 OU 9304;25;RICMS SC Art 26 I e Anexo 1 Secao I
9303;OUTRAS ARMAS DE FOGO E APARELHOS SEMELHANTES QUE UTILIZEM A DEFLAGRACAO DE POLVORA;25;RICMS SC Art 26 I e Anexo 1 Secao I
9304;OUTRAS ARMAS;25;RICMS SC Art 26 I e Anexo 1 Secao I
9305;PARTES E ACESSORIOS DOS ARTIGOS DAS POSICOES 9301 A 9304;25;RICMS SC Art 26 I e Anexo 1 Secao I
9306;BOMBAS GRANADAS TORPEDOS MINAS MISSEIS PROJETEIS E MUNICOES E SUAS PARTES INCLUINDO OS BAGOS CHUMBOS E BUCHAS PARA CARTUCHOS;25;RICMS SC Art 26 I e Anexo 1 Secao I
9307;SABRES ESPADAS BAIONETAS LANCAS E OUTRAS ARMAS BRANCAS SUAS PARTES E BAINHAS;25;RICMS SC Art 26 I e Anexo 1 Secao I

REDUÇÃO BASE DE CÁLCULO:
NCM;DESCRICAO;ALIQUOTA_ICMS;REDUCAO_BASE_CALCULO;BASE_LEGAL
01031000;Reprodutores de raca pura da especie suina vivos;12%;Reducao de 50% em saidas interestaduais;RICMS-SC/01 Anexo 2 Art 8-B
01039100;Animais vivos da especie suina de peso inferior a 50 kg;12%;Reducao de 50% em saidas interestaduais;RICMS-SC/01 Anexo 2 Art 8-B
01039200;Animais vivos da especie suina de peso igual ou superior a 50 kg;12%;Reducao de 50% em saidas interestaduais;RICMS-SC/01 Anexo 2 Art 8-B
0201;Carnes de animais da especie bovina frescas ou refrigeradas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
0202;Carnes de animais da especie bovina congeladas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
0203;Carnes de animais da especie suina frescas refrigeradas ou congeladas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
0204;Carnes de animais das especies ovina ou caprina frescas refrigeradas ou congeladas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
0206;Miudezas comestiveis de animais das especies bovina suina ovina caprina cavalar asinina e muar frescas refrigeradas ou congeladas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
0207;Carnes e miudezas comestiveis frescas resfriadas congeladas ou temperadas de aves das especies domesticas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
02101100;Pernas pernis e respectivos pedacos de suinos nao desossados (charque e carne de sol);17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
02101200;Toucinhos entremeados (entremeada) e seus pedacos de suinos (charque e carne de sol);17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
02101900;Outras carnes de suinos (charque e carne de sol);17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
02102000;Carnes da especie bovina (charque e carne de sol);17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
0401;Leite e creme de leite (nata) nao concentrados nem adicionados de acucar ou de outros edulcorantes;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
04051000;Manteiga;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
0406;Queijos e requeijao;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
04090000;Mel natural;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
07133;Feijoes (Vigna spp Phaseolus spp) secos em graos mesmo pelados ou partidos;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
09012100;Cafe torrado nao descafeinado;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
09012200;Cafe torrado descafeinado;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
090300;Mate;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
1001;Trigo e mistura de trigo com centeio (meteil);17%;Reducao de 60% do valor do imposto (importacao);RICMS-SC/01 Anexo 2 Art 15 VI a
1001;Trigo e mistura de trigo com centeio (meteil);12%;Reducao de 43,333% do valor do imposto (importacao);RICMS-SC/01 Anexo 2 Art 15 VI b
1006;Arroz;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
11010010;Farinha de trigo;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A I
11010010;Farinha de trigo;17%;Reducao de 60% do valor do imposto (importacao);RICMS-SC/01 Anexo 2 Art 15 VI a
11010010;Farinha de trigo;12%;Reducao de 43,333% do valor do imposto (importacao);RICMS-SC/01 Anexo 2 Art 15 VI b
11022000;Farinha de milho;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
11029000;Farinha de arroz;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
1502;Gorduras de animais das especies bovina ovina ou caprina em bruto ou fundidas incluindo o sebo;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
15079011;Oleo de soja refinado em recipientes com capacidade inferior ou igual a 5 litros;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
15121911;Oleo de girassol refinado em recipientes com capacidade inferior ou igual a 5 litros;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
15152910;Oleo de milho refinado em recipientes com capacidade inferior ou igual a 5 litros;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
15171000;Margarina exceto a margarina liquida;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
16041390;Manjuba boca torta (Cetengraulis edentulus) em lata;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
16041410;Sardinhas em lata;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
1701;Acucares de cana ou de beterraba e sacarose quimicamente pura no estado solido;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
19012010;Misturas e pastas para a preparacao de paes;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
19012010;Pastas de farinha de trigo para preparacao de produtos de padaria;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A XIII
19012020;Pastas de farinha de trigo para preparacao de produtos de padaria;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A XIII
19012090;Pastas de farinha de trigo para preparacao de produtos de padaria;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A XIII
19021100;Massas alimenticias nao cozidas nem recheadas ou preparadas de outro modo que contenham ovos;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
19021900;Outras massas alimenticias nao cozidas nem recheadas ou preparadas de outro modo;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
19059090;Pao;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
20098;Agua de coco;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A II
2103901;Maionese;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A II
22011000;Aguas minerais e aguas gaseificadas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A II
22029000;Nectares de frutas e outras bebidas nao alcoolicas prontas para beber exceto isotonicos e energeticos;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A II
22029000;Bebidas alimentares prontas a base de soja leite ou cacau;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A II
22090000;Vinagres e seus sucedaneos obtidos a partir do acido acetico para usos alimentares;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
25010020;Sal de mesa;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 8 VI c/c Anexo 1 Secao II
25171000;Pedra britada;17%;Reducao de 76,47% em substituicao aos creditos efetivos;RICMS-SC/01 Anexo 2 Art 7 XV
2711;Biogas e biometano;17%;Carga Tributaria Efetiva de 12%;RICMS-SC/01 Anexo 2 Art 7 XVI
3002;Produtos farmaceuticos;17%;Deducao do PIS/COFINS - 1,6082%;RICMS-SC/01 Anexo 2 Art 103 I a 1
3002;Produtos farmaceuticos;12%;Deducao do PIS/COFINS - 1,1264%;RICMS-SC/01 Anexo 2 Art 103 I a 2
3002;Produtos farmaceuticos;4%;Deducao do PIS/COFINS - 1,0382%;RICMS-SC/01 Anexo 2 Art 103 I a 3
3003;Produtos farmaceuticos;17%;Deducao do PIS/COFINS - 1,6082%;RICMS-SC/01 Anexo 2 Art 103 I a 1
3003;Produtos farmaceuticos;12%;Deducao do PIS/COFINS - 1,1264%;RICMS-SC/01 Anexo 2 Art 103 I a 2
3003;Produtos farmaceuticos;4%;Deducao do PIS/COFINS - 1,0382%;RICMS-SC/01 Anexo 2 Art 103 I a 3
3004;Produtos farmaceuticos;17%;Deducao do PIS/COFINS - 1,6082%;RICMS-SC/01 Anexo 2 Art 103 I a 1
3004;Produtos farmaceuticos;12%;Deducao do PIS/COFINS - 1,1264%;RICMS-SC/01 Anexo 2 Art 103 I a 2
3004;Produtos farmaceuticos;4%;Deducao do PIS/COFINS - 1,0382%;RICMS-SC/01 Anexo 2 Art 103 I a 3
30051010;Curativos (pensos) adesivos e outros artigos com uma camada adesiva;17%;Deducao do PIS/COFINS - 1,6082%;RICMS-SC/01 Anexo 2 Art 103 I a 1
30051010;Curativos (pensos) adesivos e outros artigos com uma camada adesiva;12%;Deducao do PIS/COFINS - 1,1264%;RICMS-SC/01 Anexo 2 Art 103 I a 2
30051010;Curativos (pensos) adesivos e outros artigos com uma camada adesiva;4%;Deducao do PIS/COFINS - 1,0382%;RICMS-SC/01 Anexo 2 Art 103 I a 3
30066000;Preparações químicas contraceptivas à base de hormônios;17%;Deducao do PIS/COFINS - 1,6082%;RICMS-SC/01 Anexo 2 Art 103 I a 1
30066000;Preparações químicas contraceptivas à base de hormônios;12%;Deducao do PIS/COFINS - 1,1264%;RICMS-SC/01 Anexo 2 Art 103 I a 2
30066000;Preparações químicas contraceptivas à base de hormônios;4%;Deducao do PIS/COFINS - 1,0382%;RICMS-SC/01 Anexo 2 Art 103 I a 3
330300;Produtos de perfumaria;17%;Deducao do PIS/COFINS - 1,9877%;RICMS-SC/01 Anexo 2 Art 103 I b 1
330300;Produtos de perfumaria;12%;Deducao do PIS/COFINS - 1,3924%;RICMS-SC/01 Anexo 2 Art 103 I b 2
330300;Produtos de perfumaria;4%;Deducao do PIS/COFINS - 1,2832%;RICMS-SC/01 Anexo 2 Art 103 I b 3
3304;Produtos de beleza ou de maquiagem;17%;Deducao do PIS/COFINS - 1,9877%;RICMS-SC/01 Anexo 2 Art 103 I b 1
3304;Produtos de beleza ou de maquiagem;12%;Deducao do PIS/COFINS - 1,3924%;RICMS-SC/01 Anexo 2 Art 103 I b 2
3304;Produtos de beleza ou de maquiagem;4%;Deducao do PIS/COFINS - 1,2832%;RICMS-SC/01 Anexo 2 Art 103 I b 3
3305;Preparações capilares;17%;Deducao do PIS/COFINS - 1,9877%;RICMS-SC/01 Anexo 2 Art 103 I b 1
3305;Preparações capilares;12%;Deducao do PIS/COFINS - 1,3924%;RICMS-SC/01 Anexo 2 Art 103 I b 2
3305;Preparações capilares;4%;Deducao do PIS/COFINS - 1,2832%;RICMS-SC/01 Anexo 2 Art 103 I b 3
330610;Dentifrícios (dentifricos);17%;Deducao do PIS/COFINS - 1,9877%;RICMS-SC/01 Anexo 2 Art 103 I b 1
330610;Dentifrícios (dentifricos);12%;Deducao do PIS/COFINS - 1,3924%;RICMS-SC/01 Anexo 2 Art 103 I b 2
330610;Dentifrícios (dentifricos);4%;Deducao do PIS/COFINS - 1,2832%;RICMS-SC/01 Anexo 2 Art 103 I b 3
330620;Fios utilizados para limpar os espaços interdentais (fios dentais);17%;Deducao do PIS/COFINS - 1,9877%;RICMS-SC/01 Anexo 2 Art 103 I b 1
330620;Fios utilizados para limpar os espaços interdentais (fios dentais);12%;Deducao do PIS/COFINS - 1,3924%;RICMS-SC/01 Anexo 2 Art 103 I b 2
330620;Fios utilizados para limpar os espaços interdentais (fios dentais);4%;Deducao do PIS/COFINS - 1,2832%;RICMS-SC/01 Anexo 2 Art 103 I b 3
330690;Outras preparações para higiene bucal ou dentária;17%;Deducao do PIS/COFINS - 1,9877%;RICMS-SC/01 Anexo 2 Art 103 I b 1
330690;Outras preparações para higiene bucal ou dentária;12%;Deducao do PIS/COFINS - 1,3924%;RICMS-SC/01 Anexo 2 Art 103 I b 2
330690;Outras preparações para higiene bucal ou dentária;4%;Deducao do PIS/COFINS - 1,2832%;RICMS-SC/01 Anexo 2 Art 103 I b 3
3307;Preparações para barbear;17%;Deducao do PIS/COFINS - 1,9877%;RICMS-SC/01 Anexo 2 Art 103 I b 1
3307;Preparações para barbear;12%;Deducao do PIS/COFINS - 1,3924%;RICMS-SC/01 Anexo 2 Art 103 I b 2
3307;Preparações para barbear;4%;Deducao do PIS/COFINS - 1,2832%;RICMS-SC/01 Anexo 2 Art 103 I b 3
39241000;Produtos de plastico para utilidades domesticas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 7 XX
39249000;Produtos de plastico para utilidades domesticas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 7 XX
4011;Pneumáticos novos de borracha;12%;Deducao do PIS/COFINS - 9,3%;RICMS-SC/01 Anexo 2 Art 103 II b
4011;Pneumáticos novos de borracha;4%;Deducao do PIS/COFINS - 8,5%;RICMS-SC/01 Anexo 2 Art 103 II c
4013;Câmaras de ar de borracha;12%;Deducao do PIS/COFINS - 9,3%;RICMS-SC/01 Anexo 2 Art 103 II b
4013;Câmaras de ar de borracha;4%;Deducao do PIS/COFINS - 8,5%;RICMS-SC/01 Anexo 2 Art 103 II c
6911;Louca outros artigos de uso domestico e artigos de higiene ou toucador de porcelana;17%;Carga Tributaria Efetiva de 8,5%;RICMS-SC/01 Anexo 2 Art 8 VIII
6911;Louca outros artigos de uso domestico e artigos de higiene ou toucador de porcelana;12%;Carga Tributaria Efetiva de 6%;RICMS-SC/01 Anexo 2 Art 8 VIII
6911;Louca outros artigos de uso domestico e artigos de higiene ou toucador de porcelana;7%;Carga Tributaria Efetiva de 3,5%;RICMS-SC/01 Anexo 2 Art 8 VIII
70132100;Copos de cristal de chumbo exceto os de vitroceramica;17%;Carga Tributaria Efetiva de 8,5%;RICMS-SC/01 Anexo 2 Art 8 VIII
70132100;Copos de cristal de chumbo exceto os de vitroceramica;12%;Carga Tributaria Efetiva de 6%;RICMS-SC/01 Anexo 2 Art 8 VIII
70132100;Copos de cristal de chumbo exceto os de vitroceramica;7%;Carga Tributaria Efetiva de 3,5%;RICMS-SC/01 Anexo 2 Art 8 VIII
70133100;Objetos para servico de mesa ou de cozinha de cristal de chumbo exceto copos e os objetos de vitroceramica;17%;Carga Tributaria Efetiva de 8,5%;RICMS-SC/01 Anexo 2 Art 8 VIII
70133100;Objetos para servico de mesa ou de cozinha de cristal de chumbo exceto copos e os objetos de vitroceramica;12%;Carga Tributaria Efetiva de 6%;RICMS-SC/01 Anexo 2 Art 8 VIII
70133100;Objetos para servico de mesa ou de cozinha de cristal de chumbo exceto copos e os objetos de vitroceramica;7%;Carga Tributaria Efetiva de 3,5%;RICMS-SC/01 Anexo 2 Art 8 VIII
73071920;Cabeca de poco para perfuracao de pocos de petroleo;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
73071920;Cabeca de poco para perfuracao de pocos de petroleo;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
73071920;Cabeca de poco para perfuracao de pocos de petroleo;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
73269000;Postes de ferro galvanizado;17%;Carga Tributaria Efetiva de 12%;RICMS-SC/01 Anexo 2 Art 7 XXI
82071900;Brocas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
82071900;Brocas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
82071900;Brocas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
82073000;Ferramentas de embutir de estampar ou de puncionar;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
82073000;Ferramentas de embutir de estampar ou de puncionar;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
82073000;Ferramentas de embutir de estampar ou de puncionar;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84021100;Caldeiras aquatubulares com producao de vapor superior a 45 toneladas por hora;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84021100;Caldeiras aquatubulares com producao de vapor superior a 45 toneladas por hora;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84021100;Caldeiras aquatubulares com producao de vapor superior a 45 toneladas por hora;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84021200;Caldeiras aquatubulares com producao de vapor nao superior a 45 toneladas por hora;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84021200;Caldeiras aquatubulares com producao de vapor nao superior a 45 toneladas por hora;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84021200;Caldeiras aquatubulares com producao de vapor nao superior a 45 toneladas por hora;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84021900;Outras caldeiras para producao de vapor incluidas as caldeiras mistas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84021900;Outras caldeiras para producao de vapor incluidas as caldeiras mistas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84021900;Outras caldeiras para producao de vapor incluidas as caldeiras mistas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84022000;Caldeiras denominadas de agua superaquecida;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84022000;Caldeiras denominadas de agua superaquecida;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84022000;Caldeiras denominadas de agua superaquecida;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84041010;Aparelhos auxiliares para caldeiras da posicao 8402;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84041010;Aparelhos auxiliares para caldeiras da posicao 8402;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84041010;Aparelhos auxiliares para caldeiras da posicao 8402;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84042000;Condensadores para maquinas a vapor;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84042000;Condensadores para maquinas a vapor;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84042000;Condensadores para maquinas a vapor;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84051000;Geradores de gas de ar (gas pobre) ou de gas de agua com ou sem depuradores; geradores de acetileno e geradores semelhantes de gas operados a agua com ou sem depuradores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84051000;Geradores de gas de ar (gas pobre) ou de gas de agua com ou sem depuradores; geradores de acetileno e geradores semelhantes de gas operados a agua com ou sem depuradores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84051000;Geradores de gas de ar (gas pobre) ou de gas de agua com ou sem depuradores; geradores de acetileno e geradores semelhantes de gas operados a agua com ou sem depuradores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84061000;Turbinas para propulsao de embarcacoes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84061000;Turbinas para propulsao de embarcacoes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84061000;Turbinas para propulsao de embarcacoes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84068100;Outras turbinas de potencia superior a 40MW;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84068100;Outras turbinas de potencia superior a 40MW;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84068100;Outras turbinas de potencia superior a 40MW;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84068200;Outras turbinas de potencia nao superior a 40MW;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84068200;Outras turbinas de potencia nao superior a 40MW;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84068200;Outras turbinas de potencia nao superior a 40MW;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84101100;Turbinas e rodas hidraulicas de potencia nao superior a 1000kW;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84101100;Turbinas e rodas hidraulicas de potencia nao superior a 1000kW;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84101100;Turbinas e rodas hidraulicas de potencia nao superior a 1000kW;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84101200;Turbinas e rodas hidraulicas de potencia superior a 1000kW mas nao superior a 10000kW;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84101200;Turbinas e rodas hidraulicas de potencia superior a 1000kW mas nao superior a 10000kW;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84101200;Turbinas e rodas hidraulicas de potencia superior a 1000kW mas nao superior a 10000kW;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84101300;Turbinas e rodas hidraulicas de potencia superior a 10000kW;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84101300;Turbinas e rodas hidraulicas de potencia superior a 10000kW;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84101300;Turbinas e rodas hidraulicas de potencia superior a 10000kW;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84109000;Reguladores para turbinas e rodas hidraulicas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84109000;Reguladores para turbinas e rodas hidraulicas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84109000;Reguladores para turbinas e rodas hidraulicas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84128000;Maquinas a vapor de embolos separadas das respectivas caldeiras;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84128000;Maquinas a vapor de embolos separadas das respectivas caldeiras;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84128000;Maquinas a vapor de embolos separadas das respectivas caldeiras;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84137010;Eletrobombas submersiveis;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84137010;Eletrobombas submersiveis;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84137010;Eletrobombas submersiveis;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84137080;Bombas centrifugas de vazao inferior ou igual a 300 litros por minuto;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84137080;Bombas centrifugas de vazao inferior ou igual a 300 litros por minuto;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84137080;Bombas centrifugas de vazao inferior ou igual a 300 litros por minuto;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84137090;Outras bombas centrifugas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84137090;Outras bombas centrifugas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84137090;Outras bombas centrifugas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84148012;Compressores de ar de parafuso;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84148012;Compressores de ar de parafuso;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84148012;Compressores de ar de parafuso;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84148013;Compressores de ar de lobulos paralelos (tipo Roots);17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84148013;Compressores de ar de lobulos paralelos (tipo Roots);12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84148013;Compressores de ar de lobulos paralelos (tipo Roots);7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84148019;Outros compressores de ar inclusive de anel liquido;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84148019;Outros compressores de ar inclusive de anel liquido;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84148019;Outros compressores de ar inclusive de anel liquido;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84148031;Compressores de gases exceto ar de pistao;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84148031;Compressores de gases exceto ar de pistao;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84148031;Compressores de gases exceto ar de pistao;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84148032;Compressores de gases exceto ar de parafuso;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84148032;Compressores de gases exceto ar de parafuso;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84148032;Compressores de gases exceto ar de parafuso;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84148033;Compressores de gases exceto ar centrifugos de vazao maxima inferior a 22000m3/h;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84148033;Compressores de gases exceto ar centrifugos de vazao maxima inferior a 22000m3/h;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84148033;Compressores de gases exceto ar centrifugos de vazao maxima inferior a 22000m3/h;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84148038;Outros compressores centrifugos radiais;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84148038;Outros compressores centrifugos radiais;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84148038;Outros compressores centrifugos radiais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84148039;Outros compressores de gases exceto ar inclusive axiais;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84148039;Outros compressores de gases exceto ar inclusive axiais;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84148039;Outros compressores de gases exceto ar inclusive axiais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84161000;Queimadores de combustiveis liquidos;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84161000;Queimadores de combustiveis liquidos;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84161000;Queimadores de combustiveis liquidos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84162010;Outros queimadores incluidos os mistos de gases;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84162010;Outros queimadores incluidos os mistos de gases;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84162010;Outros queimadores incluidos os mistos de gases;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84162090;Outros queimadores inclusive de carvao pulverizado;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84162090;Outros queimadores inclusive de carvao pulverizado;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84162090;Outros queimadores inclusive de carvao pulverizado;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84163000;Fornalhas automaticas incluidas as antefornalhas grelhas mecanicas descarregadores mecanicos de cinzas e dispositivos semelhantes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84163000;Fornalhas automaticas incluidas as antefornalhas grelhas mecanicas descarregadores mecanicos de cinzas e dispositivos semelhantes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84163000;Fornalhas automaticas incluidas as antefornalhas grelhas mecanicas descarregadores mecanicos de cinzas e dispositivos semelhantes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84169000;Ventaneiras;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84169000;Ventaneiras;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84169000;Ventaneiras;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84171010;Fornos industriais para fusao de metais;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84171010;Fornos industriais para fusao de metais;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84171010;Fornos industriais para fusao de metais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84171020;Fornos industriais para tratamento termico de metais;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84171020;Fornos industriais para tratamento termico de metais;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84171020;Fornos industriais para tratamento termico de metais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84171090;Outros fornos para tratamento termico de minerios ou de metais;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84171090;Outros fornos para tratamento termico de minerios ou de metais;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84171090;Outros fornos para tratamento termico de minerios ou de metais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84172000;Fornos de padaria pastelaria ou para a industria de bolachas e biscoitos;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84172000;Fornos de padaria pastelaria ou para a industria de bolachas e biscoitos;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84172000;Fornos de padaria pastelaria ou para a industria de bolachas e biscoitos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84178010;Fornos industriais para ceramica;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84178010;Fornos industriais para ceramica;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84178010;Fornos industriais para ceramica;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84178020;Fornos industriais para fusao de vidro;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84178020;Fornos industriais para fusao de vidro;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84178020;Fornos industriais para fusao de vidro;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84178090;Outros fornos industriais;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84178090;Outros fornos industriais;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84178090;Outros fornos industriais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84186910;Sorveteiras industriais;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84186910;Sorveteiras industriais;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84186910;Sorveteiras industriais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84186920;Resfriadores de leite;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84186920;Resfriadores de leite;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84186920;Resfriadores de leite;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84186999;Maquinas de fabricar gelo em cubos ou escamas; instalacoes frigorificas industriais formadas por elementos nao reunidos em corpo unico nem montadas sobre base comum;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84186999;Maquinas de fabricar gelo em cubos ou escamas; instalacoes frigorificas industriais formadas por elementos nao reunidos em corpo unico nem montadas sobre base comum;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84186999;Maquinas de fabricar gelo em cubos ou escamas; instalacoes frigorificas industriais formadas por elementos nao reunidos em corpo unico nem montadas sobre base comum;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84193200;Secadores para madeiras pastas de papel papeis ou cartoes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84193200;Secadores para madeiras pastas de papel papeis ou cartoes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84193200;Secadores para madeiras pastas de papel papeis ou cartoes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84193900;Outros secadores exceto para produtos agricolas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84193900;Outros secadores exceto para produtos agricolas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84193900;Outros secadores exceto para produtos agricolas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84194010;Aparelhos de destilacao de agua;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84194010;Aparelhos de destilacao de agua;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84194010;Aparelhos de destilacao de agua;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84194020;Aparelhos de destilacao ou retificacao de alcoois e outros fluidos volateis ou de hidrocarbonetos;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84194020;Aparelhos de destilacao ou retificacao de alcoois e outros fluidos volateis ou de hidrocarbonetos;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84194020;Aparelhos de destilacao ou retificacao de alcoois e outros fluidos volateis ou de hidrocarbonetos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84194090;Outros aparelhos de destilacao ou de retificacao;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84194090;Outros aparelhos de destilacao ou de retificacao;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84194090;Outros aparelhos de destilacao ou de retificacao;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84195010;Trocadores de calor de placas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84195010;Trocadores de calor de placas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84195010;Trocadores de calor de placas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84195021;Trocadores de calor tubulares metalicos;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84195021;Trocadores de calor tubulares metalicos;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84195021;Trocadores de calor tubulares metalicos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84195022;Trocadores de calor tubulares de grafite;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84195022;Trocadores de calor tubulares de grafite;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84195022;Trocadores de calor tubulares de grafite;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84195029;Outros trocadores de calor tubulares;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84195029;Outros trocadores de calor tubulares;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84195029;Outros trocadores de calor tubulares;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84195090;Outros trocadores de calor;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84195090;Outros trocadores de calor;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84195090;Outros trocadores de calor;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84196000;Aparelhos e dispositivos para liquefacao do ar ou de outros gases;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84196000;Aparelhos e dispositivos para liquefacao do ar ou de outros gases;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84196000;Aparelhos e dispositivos para liquefacao do ar ou de outros gases;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84198110;Autoclaves;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84198110;Autoclaves;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84198110;Autoclaves;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84198190;Outros aparelhos para preparacao de bebidas quentes ou para cozimento ou aquecimento de alimentos;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84198190;Outros aparelhos para preparacao de bebidas quentes ou para cozimento ou aquecimento de alimentos;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84198190;Outros aparelhos para preparacao de bebidas quentes ou para cozimento ou aquecimento de alimentos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84198911;Esterilizadores de alimentos mediante Ultra Alta Temperatura (UHT) por injecao direta de vapor com capacidade superior ou igual a 6500l/h;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84198911;Esterilizadores de alimentos mediante Ultra Alta Temperatura (UHT) por injecao direta de vapor com capacidade superior ou igual a 6500l/h;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84198911;Esterilizadores de alimentos mediante Ultra Alta Temperatura (UHT) por injecao direta de vapor com capacidade superior ou igual a 6500l/h;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84198919;Outros esterilizadores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84198919;Outros esterilizadores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84198919;Outros esterilizadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84198920;Estufas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84198920;Estufas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84198920;Estufas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84198930;Torrefadores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84198930;Torrefadores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84198930;Torrefadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84198940;Evaporadores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84198940;Evaporadores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84198940;Evaporadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84198999;Outros aparelhos e dispositivos para tratamento de materias por meio de mudanca de temperatura;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84198999;Outros aparelhos e dispositivos para tratamento de materias por meio de mudanca de temperatura;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84198999;Outros aparelhos e dispositivos para tratamento de materias por meio de mudanca de temperatura;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84201010;Calandras e laminadores para papel ou cartao;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84201010;Calandras e laminadores para papel ou cartao;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84201010;Calandras e laminadores para papel ou cartao;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84201090;Outras calandras e laminadores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84201090;Outras calandras e laminadores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84201090;Outras calandras e laminadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84209100;Cilindros para calandras e laminadores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84209100;Cilindros para calandras e laminadores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84209100;Cilindros para calandras e laminadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84211110;Desnatadeiras com capacidade de processamento de leite superior ou igual a 30000 litros por hora;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84211110;Desnatadeiras com capacidade de processamento de leite superior ou igual a 30000 litros por hora;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84211110;Desnatadeiras com capacidade de processamento de leite superior ou igual a 30000 litros por hora;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84211190;Outras desnatadeiras;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84211190;Outras desnatadeiras;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84211190;Outras desnatadeiras;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84211290;Secadores de roupa para lavanderia exceto as do codigo 84211210;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84211290;Secadores de roupa para lavanderia exceto as do codigo 84211210;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84211290;Secadores de roupa para lavanderia exceto as do codigo 84211210;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84211910;Centrifugadores para laboratorios;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84211910;Centrifugadores para laboratorios;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84211910;Centrifugadores para laboratorios;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84211990;Centrifugadores para industria acucareira; extratores centrifugos de mel;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84211990;Centrifugadores para industria acucareira; extratores centrifugos de mel;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84211990;Centrifugadores para industria acucareira; extratores centrifugos de mel;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84213990;Aparelhos para filtrar ou depurar gases;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84213990;Aparelhos para filtrar ou depurar gases;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84213990;Aparelhos para filtrar ou depurar gases;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84222000;Maquinas e aparelhos para limpar ou secar garrafas e outros recipientes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84222000;Maquinas e aparelhos para limpar ou secar garrafas e outros recipientes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84222000;Maquinas e aparelhos para limpar ou secar garrafas e outros recipientes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84223010;Maquinas e aparelhos para encher fechar capsular ou rotular garrafas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84223010;Maquinas e aparelhos para encher fechar capsular ou rotular garrafas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84223010;Maquinas e aparelhos para encher fechar capsular ou rotular garrafas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84223021;Maquinas e aparelhos para encher caixas ou sacos com po ou graos;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84223021;Maquinas e aparelhos para encher caixas ou sacos com po ou graos;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84223021;Maquinas e aparelhos para encher caixas ou sacos com po ou graos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84223022;Maquinas e aparelhos para encher e fechar embalagens confeccionadas com papel ou cartao dos codigos 48115122 ou 48115923 mesmo com dispositivo de rotulagem;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84223022;Maquinas e aparelhos para encher e fechar embalagens confeccionadas com papel ou cartao dos codigos 48115122 ou 48115923 mesmo com dispositivo de rotulagem;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84223022;Maquinas e aparelhos para encher e fechar embalagens confeccionadas com papel ou cartao dos codigos 48115122 ou 48115923 mesmo com dispositivo de rotulagem;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84223023;Maquinas e aparelhos para encher e fechar recipientes tubulares flexiveis (bisnagas) com capacidade superior ou igual a 100 unidades por minuto;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84223023;Maquinas e aparelhos para encher e fechar recipientes tubulares flexiveis (bisnagas) com capacidade superior ou igual a 100 unidades por minuto;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84223023;Maquinas e aparelhos para encher e fechar recipientes tubulares flexiveis (bisnagas) com capacidade superior ou igual a 100 unidades por minuto;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84223029;Maquinas e aparelhos para encher e fechar ampolas de vidro; outras maquinas e aparelhos para encher fechar arrolhar ou rotular caixas latas sacos ou outros recipientes capsular vasos tubos e recipientes semelhantes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84223029;Maquinas e aparelhos para encher e fechar ampolas de vidro; outras maquinas e aparelhos para encher fechar arrolhar ou rotular caixas latas sacos ou outros recipientes capsular vasos tubos e recipientes semelhantes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84223029;Maquinas e aparelhos para encher e fechar ampolas de vidro; outras maquinas e aparelhos para encher fechar arrolhar ou rotular caixas latas sacos ou outros recipientes capsular vasos tubos e recipientes semelhantes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84224010;Maquinas e aparelhos para empacotar ou embalar mercadorias horizontais proprias para empacotamento de massas alimenticias longas (comprimento superior a 200mm) em pacotes tipo almofadas (pillow pack) com capacidade de producao superior a 100 pacotes por minuto e controlador logico programavel (CLP);17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84224010;Maquinas e aparelhos para empacotar ou embalar mercadorias horizontais proprias para empacotamento de massas alimenticias longas (comprimento superior a 200mm) em pacotes tipo almofadas (pillow pack) com capacidade de producao superior a 100 pacotes por minuto e controlador logico programavel (CLP);12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84224010;Maquinas e aparelhos para empacotar ou embalar mercadorias horizontais proprias para empacotamento de massas alimenticias longas (comprimento superior a 200mm) em pacotes tipo almofadas (pillow pack) com capacidade de producao superior a 100 pacotes por minuto e controlador logico programavel (CLP);7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84224020;Maquinas e aparelhos para empacotar ou embalar mercadorias automatica para embalar tubos ou barras de metal em atados de peso inferior ou igual a 2000kg e comprimento inferior ou igual a 12m;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84224020;Maquinas e aparelhos para empacotar ou embalar mercadorias automatica para embalar tubos ou barras de metal em atados de peso inferior ou igual a 2000kg e comprimento inferior ou igual a 12m;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84224020;Maquinas e aparelhos para empacotar ou embalar mercadorias automatica para embalar tubos ou barras de metal em atados de peso inferior ou igual a 2000kg e comprimento inferior ou igual a 12m;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84224030;Maquinas e aparelhos para empacotar ou embalar mercadorias de empacotar embalagens confeccionadas com papel ou cartao dos subitens 48115122 ou 48115923 em caixas ou bandejas de papel ou cartao dobraveis com capacidade superior ou igual a 5000 embalagens por hora;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84224030;Maquinas e aparelhos para empacotar ou embalar mercadorias de empacotar embalagens confeccionadas com papel ou cartao dos subitens 48115122 ou 48115923 em caixas ou bandejas de papel ou cartao dobraveis com capacidade superior ou igual a 5000 embalagens por hora;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84224030;Maquinas e aparelhos para empacotar ou embalar mercadorias de empacotar embalagens confeccionadas com papel ou cartao dos subitens 48115122 ou 48115923 em caixas ou bandejas de papel ou cartao dobraveis com capacidade superior ou igual a 5000 embalagens por hora;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84224090;Outras maquinas e aparelhos para empacotar ou embalar mercadorias;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84224090;Outras maquinas e aparelhos para empacotar ou embalar mercadorias;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84224090;Outras maquinas e aparelhos para empacotar ou embalar mercadorias;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84232000;Basculas de pesagem continua em transportadores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84232000;Basculas de pesagem continua em transportadores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84232000;Basculas de pesagem continua em transportadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84233011;Balancas ou basculas dosadoras com aparelhos perifericos que constituam unidade funcional;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84233011;Balancas ou basculas dosadoras com aparelhos perifericos que constituam unidade funcional;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84233011;Balancas ou basculas dosadoras com aparelhos perifericos que constituam unidade funcional;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84233019;Outros dosadores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84233019;Outros dosadores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84233019;Outros dosadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84233090;Basculas de pesagem constante de grao ou liquido; outros aparelhos de pesagem constante e ensacadores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84233090;Basculas de pesagem constante de grao ou liquido; outros aparelhos de pesagem constante e ensacadores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84233090;Basculas de pesagem constante de grao ou liquido; outros aparelhos de pesagem constante e ensacadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84238110;Aparelhos e instrumentos de pesagem de capacidade nao superior a 30kg de mesa com dispositivo registrador ou impressor de etiquetas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84238110;Aparelhos e instrumentos de pesagem de capacidade nao superior a 30kg de mesa com dispositivo registrador ou impressor de etiquetas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84238110;Aparelhos e instrumentos de pesagem de capacidade nao superior a 30kg de mesa com dispositivo registrador ou impressor de etiquetas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84238190;Aparelhos verificadores de excesso ou deficiencia de peso em relacao a um padrao; outros aparelhos e instrumentos de pesagem de capacidade nao superior a 30kg;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84238190;Aparelhos verificadores de excesso ou deficiencia de peso em relacao a um padrao; outros aparelhos e instrumentos de pesagem de capacidade nao superior a 30kg;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84238190;Aparelhos verificadores de excesso ou deficiencia de peso em relacao a um padrao; outros aparelhos e instrumentos de pesagem de capacidade nao superior a 30kg;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84238200;Balança com capacidade superior a 30 kg mas não superior a 5000 kg;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84238200;Balança com capacidade superior a 30 kg mas não superior a 5000 kg;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84238200;Balança com capacidade superior a 30 kg mas não superior a 5000 kg;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84242000;Pistolas aerograficas e aparelhos semelhantes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84242000;Pistolas aerograficas e aparelhos semelhantes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84242000;Pistolas aerograficas e aparelhos semelhantes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84243010;Maquinas e aparelhos de desobstrucao de tubulacao por jato de agua;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84243010;Maquinas e aparelhos de desobstrucao de tubulacao por jato de agua;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84243010;Maquinas e aparelhos de desobstrucao de tubulacao por jato de agua;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84243020;Maquinas e aparelhos de jato de areia;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84243020;Maquinas e aparelhos de jato de areia;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84243020;Maquinas e aparelhos de jato de areia;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84243030;Perfuradoras por jato de agua com pressao de trabalho maxima superior ou igual a 10MPa;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84243030;Perfuradoras por jato de agua com pressao de trabalho maxima superior ou igual a 10MPa;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84243030;Perfuradoras por jato de agua com pressao de trabalho maxima superior ou igual a 10MPa;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84243090;Outras maquinas e aparelhos de jato de areia de jato de vapor ou qualquer outro abrasivo e aparelhos de jato semelhantes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84243090;Outras maquinas e aparelhos de jato de areia de jato de vapor ou qualquer outro abrasivo e aparelhos de jato semelhantes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84243090;Outras maquinas e aparelhos de jato de areia de jato de vapor ou qualquer outro abrasivo e aparelhos de jato semelhantes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84248990;Pulverizadores (Sprinklers) para equipamentos automaticos de combate a incendio; outros aparelhos de pulverizacao;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84248990;Pulverizadores (Sprinklers) para equipamentos automaticos de combate a incendio; outros aparelhos de pulverizacao;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84248990;Pulverizadores (Sprinklers) para equipamentos automaticos de combate a incendio; outros aparelhos de pulverizacao;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84251100;Talhas cadernais e moitoes de motor eletrico;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84251100;Talhas cadernais e moitoes de motor eletrico;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84251100;Talhas cadernais e moitoes de motor eletrico;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84251910;Talhas cadernais e moitoes manuais;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84251910;Talhas cadernais e moitoes manuais;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84251910;Talhas cadernais e moitoes manuais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84251990;Outras talhas cadernais e moitoes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84251990;Outras talhas cadernais e moitoes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84251990;Outras talhas cadernais e moitoes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84253110;Guinchos e cabrestantes de motor eletrico com capacidade inferior ou igual a 100 toneladas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84253110;Guinchos e cabrestantes de motor eletrico com capacidade inferior ou igual a 100 toneladas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84253110;Guinchos e cabrestantes de motor eletrico com capacidade inferior ou igual a 100 toneladas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84253190;Outros guinchos e cabrestantes de motor eletrico;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84253190;Outros guinchos e cabrestantes de motor eletrico;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84253190;Outros guinchos e cabrestantes de motor eletrico;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84253910;Outros guinchos e cabrestantes com capacidade inferior ou igual a 100 toneladas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84253910;Outros guinchos e cabrestantes com capacidade inferior ou igual a 100 toneladas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84253910;Outros guinchos e cabrestantes com capacidade inferior ou igual a 100 toneladas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84253990;Outros guinchos e cabrestantes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84253990;Outros guinchos e cabrestantes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84253990;Outros guinchos e cabrestantes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84261100;Pontes e vigas rolantes de suportes fixos;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84261100;Pontes e vigas rolantes de suportes fixos;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84261100;Pontes e vigas rolantes de suportes fixos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84262000;Guindastes de torre;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84262000;Guindastes de torre;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84262000;Guindastes de torre;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84263000;Guindastes de portico;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84263000;Guindastes de portico;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84263000;Guindastes de portico;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84269900;Outros guindastes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84269900;Outros guindastes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84269900;Outros guindastes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84279000;Empilhadeiras mecanicas de volumes de acao descontinua;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84279000;Empilhadeiras mecanicas de volumes de acao descontinua;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84279000;Empilhadeiras mecanicas de volumes de acao descontinua;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84281000;Elevadores de carga de uso industrial e monta-cargas;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84281000;Elevadores de carga de uso industrial e monta-cargas;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84281000;Elevadores de carga de uso industrial e monta-cargas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84282010;Transportadores tubulares (transvasadores) moveis acionados com motor de potencia superior a 90kW (120HP);17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84282010;Transportadores tubulares (transvasadores) moveis acionados com motor de potencia superior a 90kW (120HP);12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84282010;Transportadores tubulares (transvasadores) moveis acionados com motor de potencia superior a 90kW (120HP);7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84282090;Outros aparelhos elevadores ou transportadores pneumaticos;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84282090;Outros aparelhos elevadores ou transportadores pneumaticos;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84282090;Outros aparelhos elevadores ou transportadores pneumaticos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84283100;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias especialmente concebidos para uso subterraneo;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84283100;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias especialmente concebidos para uso subterraneo;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84283100;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias especialmente concebidos para uso subterraneo;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84283200;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de cacamba;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84283200;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de cacamba;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84283200;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de cacamba;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84283300;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de tira ou correia;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84283300;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de tira ou correia;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84283300;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de tira ou correia;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84283910;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de correntes;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84283910;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de correntes;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84283910;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de correntes;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84283920;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de rolos motores;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84283920;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de rolos motores;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84283920;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de rolos motores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84283930;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de pincas laterais do tipo dos utilizados para o transporte de jornais;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84283930;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de pincas laterais do tipo dos utilizados para o transporte de jornais;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84283930;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias de pincas laterais do tipo dos utilizados para o transporte de jornais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84283990;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias;17%;Reducao de 48,23% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I a
84283990;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias;12%;Reducao de 26,66% (Carga Efetiva 8,8%);RICMS-SC/01 Anexo 2 Art 9 I b
84283990;Outros aparelhos elevadores ou transportadores de acao continua para mercadorias;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 I c
84321000;Arados e charruas;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84321000;Arados e charruas;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84321000;Arados e charruas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84322100;Grades de discos;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84322100;Grades de discos;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84322100;Grades de discos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84322900;Outras grades escarificadores cultivadores extirpadores enxadas e sachadores;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84322900;Outras grades escarificadores cultivadores extirpadores enxadas e sachadores;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84322900;Outras grades escarificadores cultivadores extirpadores enxadas e sachadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84323110;Semeadores-adubadores de plantio direto;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84323110;Semeadores-adubadores de plantio direto;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84323110;Semeadores-adubadores de plantio direto;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84323190;Outros semeadores plantadores e transplantadores de plantio direto;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84323190;Outros semeadores plantadores e transplantadores de plantio direto;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84323190;Outros semeadores plantadores e transplantadores de plantio direto;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84323910;Semeadores-adubadores;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84323910;Semeadores-adubadores;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84323910;Semeadores-adubadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84323990;Outros semeadores plantadores e transplantadores;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84323990;Outros semeadores plantadores e transplantadores;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84323990;Outros semeadores plantadores e transplantadores;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84324100;Espalhadores de estrume;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84324100;Espalhadores de estrume;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84324100;Espalhadores de estrume;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84324200;Distribuidores de adubos (fertilizantes);17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84324200;Distribuidores de adubos (fertilizantes);12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84324200;Distribuidores de adubos (fertilizantes);7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84328000;Outras maquinas e aparelhos de uso agricola horticola ou florestal;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84328000;Outras maquinas e aparelhos de uso agricola horticola ou florestal;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84328000;Outras maquinas e aparelhos de uso agricola horticola ou florestal;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84332010;Ceifeiras com dispositivo de acondicionamento em fileiras;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84332010;Ceifeiras com dispositivo de acondicionamento em fileiras;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84332010;Ceifeiras com dispositivo de acondicionamento em fileiras;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84332090;Outras ceifeiras;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84332090;Outras ceifeiras;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84332090;Outras ceifeiras;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84333000;Outras maquinas e aparelhos para colher e dispor o feno;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84333000;Outras maquinas e aparelhos para colher e dispor o feno;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84333000;Outras maquinas e aparelhos para colher e dispor o feno;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84334000;Enfardadeiras de palha ou de forragem;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84334000;Enfardadeiras de palha ou de forragem;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84334000;Enfardadeiras de palha ou de forragem;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84335100;Colheitadeiras combinadas com debulhadoras (ceifeiras-debulhadoras);17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84335100;Colheitadeiras combinadas com debulhadoras (ceifeiras-debulhadoras);12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84335100;Colheitadeiras combinadas com debulhadoras (ceifeiras-debulhadoras);7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84335200;Outras maquinas e aparelhos para debulha;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84335200;Outras maquinas e aparelhos para debulha;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84335200;Outras maquinas e aparelhos para debulha;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84335300;Maquinas para colheita de raizes ou tuberculos;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84335300;Maquinas para colheita de raizes ou tuberculos;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84335300;Maquinas para colheita de raizes ou tuberculos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84335911;Colheitadeiras de algodao com capacidade para trabalhar ate dois sulcos de colheita;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84335911;Colheitadeiras de algodao com capacidade para trabalhar ate dois sulcos de colheita;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84335911;Colheitadeiras de algodao com capacidade para trabalhar ate dois sulcos de colheita;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84335919;Outras colheitadeiras de algodao;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84335919;Outras colheitadeiras de algodao;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84335919;Outras colheitadeiras de algodao;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84335990;Outras maquinas e aparelhos para colheita;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84335990;Outras maquinas e aparelhos para colheita;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84335990;Outras maquinas e aparelhos para colheita;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84336010;Selecionadores de fruta;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84336010;Selecionadores de fruta;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84336010;Selecionadores de fruta;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84336021;Maquinas para limpar ou selecionar ovos com capacidade superior a 250000 ovos por hora;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84336021;Maquinas para limpar ou selecionar ovos com capacidade superior a 250000 ovos por hora;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84336021;Maquinas para limpar ou selecionar ovos com capacidade superior a 250000 ovos por hora;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84336029;Outras maquinas para limpar ou selecionar ovos;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84336029;Outras maquinas para limpar ou selecionar ovos;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84336029;Outras maquinas para limpar ou selecionar ovos;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84336090;Outras maquinas para limpar ou selecionar produtos agricolas;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84336090;Outras maquinas para limpar ou selecionar produtos agricolas;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84336090;Outras maquinas para limpar ou selecionar produtos agricolas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84341000;Maquinas de ordenhar;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84341000;Maquinas de ordenhar;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84341000;Maquinas de ordenhar;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84361000;Maquinas e aparelhos para preparacao de alimentos ou racoes para animais;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84361000;Maquinas e aparelhos para preparacao de alimentos ou racoes para animais;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84361000;Maquinas e aparelhos para preparacao de alimentos ou racoes para animais;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84362100;Chocadeiras e criadeiras para avicultura;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84362100;Chocadeiras e criadeiras para avicultura;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84362100;Chocadeiras e criadeiras para avicultura;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84362900;Outras maquinas e aparelhos para avicultura;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84362900;Outras maquinas e aparelhos para avicultura;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84362900;Outras maquinas e aparelhos para avicultura;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
84368000;Outras maquinas e aparelhos para agricultura silvicultura avicultura ou apicultura;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
84368000;Outras maquinas e aparelhos para agricultura silvicultura avicultura ou apicultura;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
84368000;Outras maquinas e aparelhos para agricultura silvicultura avicultura ou apicultura;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
8471;Produtos de informatica e automacao;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 7 VII e XIX
8517;Produtos de informatica e automacao;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 7 VII e XIX
85381000;Quadros para medidor de luz monofasico;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A IX
8539;Lampadas eletricas;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A X
8544;Fios e cabos eletricos;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A XI
87019090;Tratores agricolas de quatro rodas;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
87019090;Tratores agricolas de quatro rodas;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
87019090;Tratores agricolas de quatro rodas;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
87162000;Reboques e semirreboques autocarregaveis ou autodescarregaveis para uso agricola;17%;Reducao de 67,05% (Carga Efetiva 5,6%);RICMS-SC/01 Anexo 2 Art 9 II a
87162000;Reboques e semirreboques autocarregaveis ou autodescarregaveis para uso agricola;12%;Reducao de 52,5% (Carga Efetiva 5,7%);RICMS-SC/01 Anexo 2 Art 9 II b
87162000;Reboques e semirreboques autocarregaveis ou autodescarregaveis para uso agricola;7%;Reducao de 26,57% (Carga Efetiva 5,14%);RICMS-SC/01 Anexo 2 Art 9 II c
8802;Aeronaves;17%;Carga Tributaria Efetiva de 4%;RICMS-SC/01 Anexo 2 Art 12
8803;Partes de aeronaves;17%;Carga Tributaria Efetiva de 4%;RICMS-SC/01 Anexo 2 Art 12
8804;Paraquedas e suas partes;17%;Carga Tributaria Efetiva de 4%;RICMS-SC/01 Anexo 2 Art 12
8805;Aparelhos e dispositivos para lancamento de aeronaves e para aterrissagem em porta-avioes e aparelhos e dispositivos semelhantes; aparelhos de treinamento de voo em terra e suas partes;17%;Carga Tributaria Efetiva de 4%;RICMS-SC/01 Anexo 2 Art 12
9018;Instrumentos e aparelhos para medicina cirurgia odontologia e veterinaria;17%;Deducao do PIS/COFINS - 1,6082%;RICMS-SC/01 Anexo 2 Art 103 I a 1
9018;Instrumentos e aparelhos para medicina cirurgia odontologia e veterinaria;12%;Deducao do PIS/COFINS - 1,1264%;RICMS-SC/01 Anexo 2 Art 103 I a 2
9018;Instrumentos e aparelhos para medicina cirurgia odontologia e veterinaria;4%;Deducao do PIS/COFINS - 1,0382%;RICMS-SC/01 Anexo 2 Art 103 I a 3
9019;Aparelhos de mecanoterapia; aparelhos de massagem; aparelhos de psicotecnica; aparelhos de ozonoterapia de oxigenoterapia de aerossolterapia aparelhos respiratorios de reanimacao e outros aparelhos de terapia respiratoria;17%;Deducao do PIS/COFINS - 1,6082%;RICMS-SC/01 Anexo 2 Art 103 I a 1
9019;Aparelhos de mecanoterapia; aparelhos de massagem; aparelhos de psicotecnica; aparelhos de ozonoterapia de oxigenoterapia de aerossolterapia aparelhos respiratorios de reanimacao e outros aparelhos de terapia respiratoria;12%;Deducao do PIS/COFINS - 1,1264%;RICMS-SC/01 Anexo 2 Art 103 I a 2
9019;Aparelhos de mecanoterapia; aparelhos de massagem; aparelhos de psicotecnica; aparelhos de ozonoterapia de oxigenoterapia de aerossolterapia aparelhos respiratorios de reanimacao e outros aparelhos de terapia respiratoria;4%;Deducao do PIS/COFINS - 1,0382%;RICMS-SC/01 Anexo 2 Art 103 I a 3
9021;Artigos e aparelhos ortopedicos incluindo as cintas e fundas medico-cirurgicas e as muletas; talas goteiras e outros artigos e aparelhos para fraturas; artigos e aparelhos de protese; aparelhos para facilitar a audicao dos surdos e outros aparelhos para compensar uma deficiencia ou uma incapacidade destinados a serem transportados a mao ou sobre as pessoas ou a serem implantados no organismo;17%;Deducao do PIS/COFINS - 1,6082%;RICMS-SC/01 Anexo 2 Art 103 I a 1
9021;Artigos e aparelhos ortopedicos incluindo as cintas e fundas medico-cirurgicas e as muletas; talas goteiras e outros artigos e aparelhos para fraturas; artigos e aparelhos de protese; aparelhos para facilitar a audicao dos surdos e outros aparelhos para compensar uma deficiencia ou uma incapacidade destinados a serem transportados a mao ou sobre as pessoas ou a serem implantados no organismo;12%;Deducao do PIS/COFINS - 1,1264%;RICMS-SC/01 Anexo 2 Art 103 I a 2
9021;Artigos e aparelhos ortopedicos incluindo as cintas e fundas medico-cirurgicas e as muletas; talas goteiras e outros artigos e aparelhos para fraturas; artigos e aparelhos de protese; aparelhos para facilitar a audicao dos surdos e outros aparelhos para compensar uma deficiencia ou uma incapacidade destinados a serem transportados a mao ou sobre as pessoas ou a serem implantados no organismo;4%;Deducao do PIS/COFINS - 1,0382%;RICMS-SC/01 Anexo 2 Art 103 I a 3
9022;Aparelhos de raios X e aparelhos que utilizem radiacoes alfa beta ou gama;17%;Deducao do PIS/COFINS - 1,6082%;RICMS-SC/01 Anexo 2 Art 103 I a 1
9022;Aparelhos de raios X e aparelhos que utilizem radiacoes alfa beta ou gama;12%;Deducao do PIS/COFINS - 1,1264%;RICMS-SC/01 Anexo 2 Art 103 I a 2
9022;Aparelhos de raios X e aparelhos que utilizem radiacoes alfa beta ou gama;4%;Deducao do PIS/COFINS - 1,0382%;RICMS-SC/01 Anexo 2 Art 103 I a 3
94054090;Luminarias;17%;Carga Tributaria Efetiva de 7%;RICMS-SC/01 Anexo 2 Art 11-A XII
96032100;Escovas de dentes;17%;Deducao do PIS/COFINS - 1,9877%;RICMS-SC/01 Anexo 2 Art 103 I b 1
96032100;Escovas de dentes;12%;Deducao do PIS/COFINS - 1,3924%;RICMS-SC/01 Anexo 2 Art 103 I b 2
96190000;Absorventes e tampoes higienicos;17%;Deducao do PIS/COFINS - 1,9877%;RICMS-SC/01 Anexo 2 Art 103 I b 1
96190000;Absorventes e tampoes higienicos;12%;Deducao do PIS/COFINS - 1,3924%;RICMS-SC/01 Anexo 2 Art 103 I b 2

ISENÇÕES:
NCM;DESCRIÇÃO;ALÍQUOTA ICMS;ISENÇÃO;OUTRAS PARTICULARIDADES;BASE LEGAL
0102.21.10;REPRODUTOR BOVINO DE RACA PURA PRENHE OU COM CRIA AO PE;zero;SIM;Importacao de reprodutor ou matriz de bovino puro de origem ou puro por cruza;Anexo 2 Art 3 Inciso II
0102.21.90;OUTROS REPRODUTORES BOVINOS DE RACA PURA;zero;SIM;Importacao de reprodutor ou matriz de bovino puro de origem ou puro por cruza;Anexo 2 Art 3 Inciso II
0102.29.11;REPRODUTOR BOVINO PRENHE OU COM CRIA AO PE;zero;SIM;Saida interestadual de reprodutor ou matriz de bovino puro de origem ou puro por cruza com registro genealogico oficial;Anexo 2 Art 2 Inciso IV
0102.29.19;OUTROS REPRODUTORES BOVINOS;zero;SIM;Saida interestadual de reprodutor ou matriz de bovino puro de origem ou puro por cruza com registro genealogico oficial;Anexo 2 Art 2 Inciso IV
0102.31.10;REPRODUTOR BUFALINO DE RACA PURA PRENHE OU COM CRIA AO PE;zero;SIM;Importacao de reprodutor ou matriz de bufalino puro de origem ou puro por cruza;Anexo 2 Art 3 Inciso II
0102.31.90;OUTROS REPRODUTORES BUFALINOS DE RACA PURA;zero;SIM;Importacao de reprodutor ou matriz de bufalino puro de origem ou puro por cruza;Anexo 2 Art 3 Inciso II
0102.39.11;REPRODUTOR BUFALINO PRENHE OU COM CRIA AO PE;zero;SIM;Saida interestadual de reprodutor ou matriz de bufalino puro de origem ou puro por cruza com registro genealogico oficial;Anexo 2 Art 2 Inciso IV
0102.39.19;OUTROS REPRODUTORES BUFALINOS;zero;SIM;Saida interestadual de reprodutor ou matriz de bufalino puro de origem ou puro por cruza com registro genealogico oficial;Anexo 2 Art 2 Inciso IV
0103.10.00;REPRODUTORES SUINOS DE RACA PURA;zero;SIM;Importacao de reprodutor ou matriz de suino puro de origem ou puro por cruza;Anexo 2 Art 3 Inciso II
0103.10.00;REPRODUTORES SUINOS DE RACA PURA;zero;SIM;Saida interestadual de reprodutor ou matriz de suino puro de origem ou puro por cruza com registro genealogico oficial;Anexo 2 Art 2 Inciso IV
0104.10.11;REPRODUTOR OVINO DE RACA PURA PRENHE OU COM CRIA AO PE;zero;SIM;Importacao de reprodutor ou matriz de ovino puro de origem ou puro por cruza;Anexo 2 Art 3 Inciso II
0104.10.19;OUTROS REPRODUTORES OVINOS DE RACA PURA;zero;SIM;Importacao de reprodutor ou matriz de ovino puro de origem ou puro por cruza;Anexo 2 Art 3 Inciso II
0104.10.19;OUTROS REPRODUTORES OVINOS DE RACA PURA;zero;SIM;Saida interestadual de reprodutor ou matriz de ovino puro de origem ou puro por cruza com registro genealogico oficial;Anexo 2 Art 2 Inciso IV
0104.20.10;REPRODUTORES DE RACA PURA CAPRINOS;zero;SIM;Importacao de matriz e reprodutor de caprino de comprovada superioridade genetica enquanto vigorar o Convenio ICMS 20/92;Anexo 2 Art 3 Inciso III
0307.11.00;OSTRAS FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interna em estado natural resfriado ou congelado enquanto vigorar o Convenio ICMS 147/92;Anexo 2 Art 1 Inciso II
0307.21.00;VIEIRAS FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interna em estado natural resfriado ou congelado enquanto vigorar o Convenio ICMS 147/92;Anexo 2 Art 1 Inciso II
0307.31.00;MEXILHOES FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interna em estado natural resfriado ou congelado enquanto vigorar o Convenio ICMS 147/92;Anexo 2 Art 1 Inciso II
0307.42.00;BERBIGAO FRESCO OU REFRIGERADO;zero;SIM;Operacao interna em estado natural resfriado ou congelado enquanto vigorar o Convenio ICMS 147/92;Anexo 2 Art 1 Inciso II
0307.91.00;MARISCOS FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interna em estado natural resfriado ou congelado enquanto vigorar o Convenio ICMS 147/92;Anexo 2 Art 1 Inciso II
0401.10.10;LEITE UHT COM TEOR DE MATERIA GORDA NAO SUPERIOR A 1 POR CENTO EM PESO;zero;SIM;Operacao interna de leite fresco pasteurizado ou nao destinada a consumidor final;Anexo 2 Art 1 Inciso I
0401.20.10;LEITE UHT COM TEOR DE MATERIA GORDA SUPERIOR A 1 POR CENTO MAS NAO SUPERIOR A 6 POR CENTO EM PESO;zero;SIM;Operacao interna de leite fresco pasteurizado ou nao destinada a consumidor final;Anexo 2 Art 1 Inciso I
0401.40.10;LEITE COM TEOR DE MATERIA GORDA SUPERIOR A 6 POR CENTO MAS NAO SUPERIOR A 10 POR CENTO EM PESO;zero;SIM;Operacao interna de leite fresco pasteurizado ou nao destinada a consumidor final;Anexo 2 Art 1 Inciso I
0401.50.10;LEITE COM TEOR DE MATERIA GORDA SUPERIOR A 10 POR CENTO EM PESO;zero;SIM;Operacao interna de leite fresco pasteurizado ou nao destinada a consumidor final;Anexo 2 Art 1 Inciso I
0402.10.10;LEITE EM PO COM TEOR DE ARSENIO CHUMBO OU COBRE INFERIOR A 5 PPM;zero;SIM;Operacao interna de leite reconstituido destinado a consumidor final mantido o credito fiscal na entrada do leite em po de 1 de marco a 30 de setembro;Anexo 2 Art 1 Inciso I
0407.21.00;OVOS FRESCOS DE AVES DA ESPECIE GALLUS DOMESTICUS;zero;SIM;Operacao interestadual exceto quando destinados a industrializacao nao se exigindo estorno de credito;Anexo 2 Art 2 Inciso II
0407.29.00;OUTROS OVOS FRESCOS;zero;SIM;Operacao interestadual exceto quando destinados a industrializacao nao se exigindo estorno de credito;Anexo 2 Art 2 Inciso II
0701.90.00;BATATAS FRESCAS OU REFRIGERADAS EXCETO PARA SEMENTEIRA;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0702.00.00;TOMATES FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0703.10.19;OUTRAS CEBOLAS FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0703.20.90;OUTROS ALHOS FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0703.90.90;OUTROS ALHOS-PORO E OUTROS PRODUTOS HORTICOLAS ALHACEOS FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0704.10.00;COUVE-FLOR E BROCOLOS FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0704.90.00;OUTRAS COUVES FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0705.11.00;ALFACE REPOLHUDA FRESCA OU REFRIGERADA;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0705.19.00;OUTRA ALFACE FRESCA OU REFRIGERADA;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0705.21.00;CHICORIA WITLOOF FRESCA OU REFRIGERADA;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0705.29.00;OUTRAS CHICORIAS FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0706.10.00;CENOURAS E NABOS FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0706.90.00;BETERRABAS PARA SALADA E OUTRAS RAIZES COMESTIVEIS FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0707.00.00;PEPINOS E PEPININHOS (CORNICHONS) FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0708.10.00;ERVILHAS COM VAGEM FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0708.20.00;FEIJOES EM VAGEM FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0709.20.00;ASPARGOS FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0709.30.00;BERINJELAS FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0709.40.00;AIPO EXCETO AIPO-RABANO FRESCO OU REFRIGERADO;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0709.51.00;COGUMELOS DO GENERO AGARICUS FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0709.60.00;PIMENTOES E PIMENTAS DO GENERO CAPSICUM FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0709.70.00;ESPINAFRES FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0709.92.00;ALCACHOFRAS FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0709.93.00;ABOBORAS ABOBRINHAS E CABACAS FRESCAS OU REFRIGERADAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0709.99.90;OUTROS PRODUTOS HORTICOLAS FRESCOS OU REFRIGERADOS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0714.10.00;RAIZES DE MANDIOCA FRESCAS REFRIGERADAS CONGELADAS OU SECAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0714.20.00;BATATAS-DOCES FRESCAS REFRIGERADAS CONGELADAS OU SECAS;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0714.30.00;INHAME FRESCO REFRIGERADO CONGELADO OU SECO;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0714.40.00;TARO (COLOCASIA SPP) FRESCO REFRIGERADO CONGELADO OU SECO;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao;Anexo 2 Art 2 Inciso I
0804.50.20;MANGAS FRESCAS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0805.10.00;LARANJAS FRESCAS OU SECAS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0805.21.00;MANDARINAS FRESCAS OU SECAS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0805.40.00;TORANJAS E POMELOS FRESCOS OU SECOS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0805.50.00;LIMOES E LIMAS FRESCAS OU SECAS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0806.10.00;UVAS FRESCAS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0807.11.00;MELANCIAS FRESCAS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0807.19.00;MELOES FRESCOS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0808.30.00;PERAS FRESCAS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0808.40.00;MARMELOS FRESCOS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0809.10.00;DAMASCOS FRESCOS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0809.29.00;OUTRAS CEREJAS FRESCAS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0809.30.10;PESSEGOS FRESCOS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0809.40.10;AMEIXAS FRESCAS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0810.10.00;MORANGOS FRESCOS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0810.70.00;CAQUIS (DIOSPIROS) FRESCOS;zero;SIM;Importacao de frutas frescas de paises membros da ALADI exceto amendoa avela castanha maca noz e pera;Anexo 2 Art 3 Inciso I
0813.50.00;MISTURAS DE FRUTAS SECAS OU DE FRUTAS DE CASCA RIJA DO CAPITULO 8;zero;SIM;Operacao interestadual em estado natural exceto quando destinadas a industrializacao e exceto amendoa avela castanha e noz;Anexo 2 Art 2 Inciso I
0901.11.10;CAFE NAO TORRADO EM GRAO NAO DESCAFEINADO;zero;SIM;Operacao interestadual em estado natural exceto quando destinado a industrializacao;Anexo 2 Art 2 Inciso I
1212.99.90;PINHAO;zero;SIM;Operacao interestadual em estado natural exceto quando destinado a industrializacao;Anexo 2 Art 2 Inciso I
2201.10.00;AGUAS MINERAIS E AGUAS GASEIFICADAS;zero;SIM;Saida ou fornecimento de agua natural proveniente de servico publico de captacao tratamento e distribuicao;Anexo 2 Art 2 Inciso XVI
2201.90.00;OUTRAS AGUAS INCLUINDO AGUAS MINERAIS NATURAIS OU ARTIFICIAIS E AGUAS GASEIFICADAS;zero;SIM;Saida ou fornecimento de agua natural proveniente de servico publico de captacao tratamento e distribuicao;Anexo 2 Art 2 Inciso XVI
2801.20.90;IODO METALICO;zero;SIM;Importacao de iodo metalico;Anexo 2 Art 3 Inciso IV
2902.90.90;CICLOPROPIL-ACETILENO;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2924.29.99;SULFATO DE INDINAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.39.29;CLORIDRATO DE 3-CLORO-METILPIRIDINA E OUTROS;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.39.99;SULFATO DE ATAZANAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.49.90;BENZOATO DE N-(1 1-DIMETILETIL) DECAHIDRO-2-(2-HIDROXI-3-AMINO-4-(FENILTIOBUTIL)-3-ISOQUINOLI-NA CARBOXAMIDA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.59.19;INDINAVIR BASE;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.59.49;FUMARATO DE TENOFOVIR DESOPROXILA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.59.49;GANCICLOVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.59.49;TENOFOVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.59.99;CITOSINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.59.99;ETRAVIRINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2933.99.99;EFAVIRENZ;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2934.99.22;ZIDOVUDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2934.99.23;TIMIDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2934.99.27;ESTAVUDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2934.99.29;DIDANOSINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2934.99.29;ENTRICITABINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2934.99.39;HIDROXIBENZOATO DE (2R-CIS)-4-AMINO-1--2(1H)-PIRIMIDINONA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2934.99.93;LAMIVUDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2934.99.99;NEVIRAPINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
2934.99.99;(2R 5R)-5-(4-AMINO-2-OXO-2H-PIRIMIDIN-1-IL)-[1 3]-OXATIOLAN-2-CARBOXILATO DE 2S-ISOPROPIL-5R-METIL 1R-CICLOHEXILA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.69;MEDICAMENTO COM LOPINAVIR E RITONAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.78;MESILATO DE NELFINAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.78;SAQUINAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.78;SULFATO DE ABACAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.78;SULFATO DE INDINAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.78;FUMARATO DE TENOFOVIR DESOPROXILA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.79;EFAVIRENZ;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.79;RITONAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.79;ZIAGENAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.88;FOSAMPRENAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.99;DELAVIRDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.99;DIDANOSINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.99;ESTAVUDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.99;LAMIVUDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3003.90.99;ZALCITABINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.59;MEDICAMENTO COM LOPINAVIR E RITONAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.68;ENFURVITIDA T-20;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.68;FUMARATO DE TENOFOVIR DESOPROXILA E ENTRICITABINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.68;MESILATO DE NELFINAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.68;SAQUINAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.68;SULFATO DE ABACAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.68;SULFATO DE INDINAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.69;EFAVIRENZ;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.69;MARAVIROQUE;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.69;RITONAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.69;ZIAGENAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.78;FOSAMPRENAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.79;DARUNAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.79;NEVIRAPINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.79;RALTEGRAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.79;TIPRANAVIR;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.79;ZIDOVUDINA AZT;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.99;DELAVIRDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.99;DIDANOSINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.99;ESTAVUDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.99;LAMIVUDINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3004.90.99;ZALCITABINA;zero;SIM;Operacao com farmacos e medicamentos da Secao XXVI do Anexo 1 destinados a orgaos da administracao publica condicionado a desoneracao de PIS/COFINS e deducao do preco;Anexo 2 Art 2 Inciso XLIX
3504.00.90;ALBUMINA HUMANA;zero;SIM;Operacao com medicamentos e reagentes quimicos da Secao XXXIII do Anexo 1 para pesquisas com seres humanos condicionado a registro na ANVISA e desoneracao de PIS/PASEP e COFINS;Anexo 2 Art 2 Inciso LVI
3808.91.99;INSETICIDAS;zero;SIM;Saida interestadual de inseticida fungicida formicida herbicida parasiticida germicida acaricida nematicida raticida e desfolhante para uso na agropecuaria;Anexo 2 Art 2 Inciso V
3808.92.99;FUNGICIDAS;zero;SIM;Saida interestadual de inseticida fungicida formicida herbicida parasiticida germicida acaricida nematicida raticida e desfolhante para uso na agropecuaria;Anexo 2 Art 2 Inciso V
3808.93.29;HERBICIDAS;zero;SIM;Saida interestadual de inseticida fungicida formicida herbicida parasiticida germicida acaricida nematicida raticida e desfolhante para uso na agropecuaria;Anexo 2 Art 2 Inciso V
3822.19.90;REAGENTES DE LABORATORIO;zero;SIM;Operacao com medicamentos e reagentes quimicos da Secao XXXIII do Anexo 1 para pesquisas com seres humanos condicionado a registro na ANVISA e desoneracao de PIS/PASEP e COFINS;Anexo 2 Art 2 Inciso LVI
3824.99.77;ADUBOS FOLIARES;zero;SIM;Saida interestadual de adubo simples ou composto e fertilizantes;Anexo 2 Art 2 Inciso V
3923.21.90;SACO DE POLIETILENO;zero;SIM;Operacao interna de saida de vasilhames sacarias e embalagens vazios destinados ao acondicionamento de produtos industrializados ou agropecuarios;Anexo 2 Art 1 Inciso V
3923.90.00;EMBALAGEM DE AGROTOXICO USADA E LAVADA;zero;SIM;Saida de embalagem de agrotoxico usada e lavada com destino a centrais ou postos de coleta e estabelecimentos recicladores;Anexo 2 Art 2 Inciso XLVI
3923.90.00;EMBALAGEM DE AGROTOXICO USADA E LAVADA;zero;SIM;Saida interestadual de embalagem de agrotoxico usada e lavada com destino a centrais ou postos de coleta e estabelecimentos recicladores;Anexo 2 Art 5 Inciso XIV
4014.10.00;PRESERVATIVOS;zero;SIM;Operacao interestadual de preservativos classificados no codigo 4014.10.00;Anexo 2 Art 2 Inciso XXXI
4819.40.00;SACO DE PAPEL;zero;SIM;Operacao interna de saida de vasilhames sacarias e embalagens vazios destinados ao acondicionamento de produtos industrializados ou agropecuarios;Anexo 2 Art 1 Inciso V
7311.00.00;BOTIJAO PARA GLP;zero;SIM;Saida relacionada com a destroca de botijoes vazios para acondicionamento de GLP promovida por distribuidor de gas e seus revendedores credenciados;Anexo 2 Art 2 Inciso VIII
8424.41.00;PULVERIZADORES PARA AGRICULTURA OU HORTICULTURA;zero;SIM;Saida interestadual de maquinas e implementos agricolas;Anexo 2 Art 2 Inciso V
8432.10.00;ARADOS E CHARRUAS;zero;SIM;Saida interestadual de maquinas e implementos agricolas;Anexo 2 Art 2 Inciso V
8432.31.10;SEMEADORES-ADUBADORES DE PLANTIO DIRETO;zero;SIM;Saida interestadual de maquinas e implementos agricolas;Anexo 2 Art 2 Inciso V
8433.51.00;COLHEITADEIRAS COMBINADAS COM DEBULHADORAS;zero;SIM;Saida interestadual de maquinas e implementos agricolas;Anexo 2 Art 2 Inciso V
8537.20.00;SUBESTACAO ISOLADA A GAS SF6;zero;SIM;Importacao e subsequente saida interna de Subestacao Isolada a Gas SF6 destinada a Usina Hidreletrica de Machadinho sem similar produzido no pais;Anexo 2 Art 86
8602.10.00;LOCOMOTIVA DIESEL-ELETRICA COM POTENCIA MAXIMA SUPERIOR A 3000 HP;zero;SIM;Saida de locomotiva diesel-eletrica com potencia maxima superior a 3000 HP enquanto vigorar o Convenio ICMS 32/06;Anexo 2 Art 2 Inciso LXII
8702.10.00;VEICULOS AUTOMOVEIS PARA TRANSPORTE DE DEZ PESSOAS OU MAIS INCLUINDO O MOTORISTA COM MOTOR DE PISTAO DE IGNICAO POR COMPRESSAO (DIESEL OU SEMIDIESEL);zero;SIM;Operacao com onibus micro-onibus e embarcacoes destinados ao transporte escolar no ambito do Programa Caminho da Escola do MEC;Anexo 2 Art 4 Inciso XV
8703.21.00;AUTOMOVEIS DE PASSAGEIROS DE CILINDRADA NAO SUPERIOR A 1000 CM3;zero;SIM;Operacao interna de saida de veiculo novo adquirido pela Secretaria de Seguranca Publica ou Secretaria da Fazenda para reequipamento dispensado estorno de credito;Anexo 2 Art 1 Inciso III
8703.22.10;AUTOMOVEIS DE PASSAGEIROS COM MOTOR A PISTAO DE IGNICAO POR CENTELHA DE CILINDRADA SUPERIOR A 1000 CM3 MAS NAO SUPERIOR A 1500 CM3 COM CAPACIDADE DE TRANSPORTE DE PESSOAS SENTADAS INFERIOR OU IGUAL A SEIS INCLUINDO O CONDUTOR;zero;SIM;Operacao interna de saida de veiculo novo adquirido pela Secretaria de Seguranca Publica ou Secretaria da Fazenda para reequipamento dispensado estorno de credito;Anexo 2 Art 1 Inciso III
8703.22.90;OUTROS AUTOMOVEIS DE PASSAGEIROS COM MOTOR A PISTAO DE IGNICAO POR CENTELHA DE CILINDRADA SUPERIOR A 1000 CM3 MAS NAO SUPERIOR A 1500 CM3;zero;SIM;Operacao interna de saida de veiculo novo adquirido pela Secretaria de Seguranca Publica ou Secretaria da Fazenda para reequipamento dispensado estorno de credito;Anexo 2 Art 1 Inciso III
8713.10.00;CADEIRAS DE RODAS E OUTROS VEICULOS PARA PESSOAS COM INCAPACIDADE SEM MECANISMO DE PROPULSAO;zero;SIM;Operacao interestadual de equipamentos e acessorios listados na Secao IX do Anexo 1 dispensado estorno de credito;Anexo 2 Art 2 Inciso XV
8713.90.00;OUTRAS CADEIRAS DE RODAS E OUTROS VEICULOS PARA PESSOAS COM INCAPACIDADE;zero;SIM;Operacao interestadual de equipamentos e acessorios listados na Secao IX do Anexo 1 dispensado estorno de credito;Anexo 2 Art 2 Inciso XV
9018.19.80;EQUIPAMENTOS DE ELETRODIAGNOSTICO;zero;SIM;Operacao com medicamentos e reagentes quimicos da Secao XXXIII do Anexo 1 para pesquisas com seres humanos condicionado a registro na ANVISA e desoneracao de PIS/PASEP e COFINS;Anexo 2 Art 2 Inciso LVI
9018.90.99;OUTROS INSTRUMENTOS E APARELHOS PARA MEDICINA CIRURGIA ODONTOLOGIA E VETERINARIA;zero;SIM;Operacao com medicamentos e reagentes quimicos da Secao XXXIII do Anexo 1 para pesquisas com seres humanos condicionado a registro na ANVISA e desoneracao de PIS/PASEP e COFINS;Anexo 2 Art 2 Inciso LVI
9021.10.10;ARTIGOS E APARELHOS ORTOPEDICOS;zero;SIM;Operacao interestadual de equipamentos e acessorios listados na Secao IX do Anexo 1 dispensado estorno de credito;Anexo 2 Art 2 Inciso XV
9021.31.10;PROTESES Femorais;zero;SIM;Operacao interestadual de equipamentos e acessorios listados na Secao IX do Anexo 1 dispensado estorno de credito;Anexo 2 Art 2 Inciso XV
9027.89.99;OUTROS INSTRUMENTOS E APARELHOS PARA ANALISES FISICAS OU QUIMICAS;zero;SIM;Operacao com medicamentos e reagentes quimicos da Secao XXXIII do Anexo 1 para pesquisas com seres humanos condicionado a registro na ANVISA e desoneracao de PIS/PASEP e COFINS;Anexo 2 Art 2 Inciso LVI
9307.00.00;FOGUETE ANTIGRANIZO;zero;SIM;Importacao de foguetes antigranizo e respectivas rampas ou plataformas de lancamento;Anexo 2 Art 3 Inciso V
9701.21.00;PINTURAS E DESENHOS FEITOS INTEIRAMENTE A MAO;zero;SIM;Saida de obra de arte decorrente de operacao realizada pelo proprio autor;Anexo 2 Art 2 Inciso XVII
9701.21.00;PINTURAS E DESENHOS FEITOS INTEIRAMENTE A MAO;zero;SIM;Saida de mercadoria em decorrencia de doacao a entidades governamentais para assistencia a vitimas de calamidade publica;Anexo 2 Art 5 Inciso III
9702.10.00;GRAVURAS ESTAMPAS E LITOGRAFIAS ORIGINAIS COM MAIS DE 100 ANOS;zero;SIM;Saida de obra de arte decorrente de operacao realizada pelo proprio autor;Anexo 2 Art 2 Inciso XVII
9703.10.00;OBRAS DE ESTATUARIA OU DE ESCULTURA ORIGINAIS COM MAIS DE 100 ANOS;zero;SIM;Saida de obra de arte decorrente de operacao realizada pelo proprio autor;Anexo 2 Art 2 Inciso XVII
9999.99.99;BENS E MERCADORIAS DIVERSAS;zero;SIM;Saida de bens e mercadorias destinadas aos orgaos da administracao publica estadual direta e suas fundacoes e autarquias;Anexo 2 Art 1 Inciso XI
9999.99.99;BENS E MERCADORIAS DIVERSAS;zero;SIM;Saida de mercadorias em decorrencia de doacao a orgaos e entidades da administracao publica ou entidades assistenciais de utilidade publica;Anexo 2 Art 2 Inciso XLI
9999.99.99;BENS E MERCADORIAS DIVERSAS;zero;SIM;Saida de mercadorias em decorrencia de doacao a orgaos e entidades da administracao publica ou entidades assistenciais de utilidade publica do pais;Anexo 2 Art 5 Inciso V
9999.99.99;BENS E MERCADORIAS DIVERSAS;zero;SIM;Recebimento de mercadoria ou bem importado do exterior que retorne ao pais por nao ter sido possivel a entrega ao destinatario;Anexo 2 Art 6 Inciso I
9999.99.99;BENS E MERCADORIAS DIVERSAS;zero;SIM;Recebimento de mercadoria ou bem estrangeiro identico em reposicao a outro importado com imposto pago que se revelou defeituoso;Anexo 2 Art 6 Inciso II
9999.99.99;BENS E MERCADORIAS DIVERSAS;zero;SIM;Ingresso de bens procedentes do exterior integrantes de bagagem de viajante;Anexo 2 Art 6 Inciso VI
9999.99.99;MAQUINAS EQUIPAMENTOS APARELHOS INSTRUMENTOS OU MATERIAL E SEUS ACESSORIOS;zero;SIM;Operacoes com maquina equipamento aparelho instrumento ou material e seus acessorios sobressalentes ou ferramentas para integrar o ativo imobilizado de empresa industrial com BEFIEX aprovado ate 31 de dezembro de 1989;Anexo 2 Art 50
9999.99.99;MEDICAMENTOS DIVERSOS;zero;SIM;Recebimento de medicamentos importados do exterior por pessoa fisica para uso humano proprio ou individual;Anexo 2 Art 6 Inciso V
9999.99.99;MERCADORIA IMPORTADA SOB DRAWBACK;zero;SIM;Entrada de mercadoria importada sob o regime aduaneiro especial na modalidade drawback integrado suspensao empregada ou consumida no processo de industrializacao cujo produto resultante seja exportado;Anexo 2 Art 46
9999.99.99;AMOSTRA SEM VALOR COMERCIAL;zero;SIM;Recebimento de amostra do exterior sem valor comercial conforme legislacao federal que outorga isencao do Imposto de Importacao;Anexo 2 Art 6 Inciso III
9999.99.99;PRODUTO DO TRABALHO DE DETENTOS;zero;SIM;Saida de produto resultante do trabalho de reeducacao dos detentos promovida pelos estabelecimentos do Sistema Penitenciario do Estado;Anexo 2 Art 1 Inciso VIII

SUBSTITUIÇÃO TRIBUTÁRIA:
NCM;DESCRIÇÃO;SUBSTITUIÇÃO TRIBUTÁRIA;MVA ORIGINAL;BASE LEGAL
04011010;Leite UHT Ultra High Temperature;SIM;N/A;Anexo 1-A Secao XVII
04011090;Outro leite UHT Ultra High Temperature;SIM;N/A;Anexo 1-A Secao XVII
04012010;Leite UHT Ultra High Temperature;SIM;N/A;Anexo 1-A Secao XVII
04012090;Outros leites UHT Ultra High Temperature;SIM;N/A;Anexo 1-A Secao XVII
04014010;Leite;SIM;N/A;Anexo 1-A Secao XVII
04014021;Creme de leite nata UHT Ultra High Temperature;SIM;N/A;Anexo 1-A Secao XVII
04014029;Outros cremes de leite nata;SIM;N/A;Anexo 1-A Secao XVII
04015010;Leite;SIM;N/A;Anexo 1-A Secao XVII
04015021;Creme de leite nata UHT Ultra High Temperature;SIM;N/A;Anexo 1-A Secao XVII
04015029;Outros cremes de leite nata;SIM;N/A;Anexo 1-A Secao XVII
04021010;Leite em po granulos ou outras formas solidas com um teor de materias gordas nao superior a 1,5% com um teor de arsenio chumbo ou cobre considerados isoladamente inferior a 5 ppm;SIM;N/A;Anexo 1-A Secao XVII
04021090;Outros leites em po granulos ou outras formas solidas com um teor de materias gordas nao superior a 1,5%;SIM;N/A;Anexo 1-A Secao XVII
04022110;Leite integral em po granulos ou outras formas solidas sem adicao de acucar ou de outros edulcorantes;SIM;N/A;Anexo 1-A Secao XVII
04022120;Leite parcialmente desnatado em po granulos ou outras formas solidas sem adicao de acucar ou de outros edulcorantes;SIM;N/A;Anexo 1-A Secao XVII
04022130;Creme de leite nata em po granulos ou outras formas solidas sem adicao de acucar ou de outros edulcorantes;SIM;N/A;Anexo 1-A Secao XVII
04022910;Leite integral em po granulos ou outras formas solidas com adicao de acucar ou de outros edulcorantes;SIM;N/A;Anexo 1-A Secao XVII
04022920;Leite parcialmente desnatado em po granulos ou outras formas solidas com adicao de acucar ou de outros edulcorantes;SIM;N/A;Anexo 1-A Secao XVII
04022930;Creme de leite nata em po granulos ou outras formas solidas com adicao de acucar ou de outros edulcorantes;SIM;N/A;Anexo 1-A Secao XVII
04029100;Leite e creme de leite nata concentrados ou adicionados de acucar ou de outros edulcorantes sem adicao de acucar ou de outros edulcorantes;SIM;N/A;Anexo 1-A Secao XVII
04029900;Outros leites e cremes de leite nata concentrados ou adicionados de acucar ou de outros edulcorantes;SIM;N/A;Anexo 1-A Secao XVII
04032000;Iogurte;SIM;N/A;Anexo 1-A Secao XVII
04039000;Outros leites e cremes de leite natas fermentados ou acidificados;SIM;N/A;Anexo 1-A Secao XVII
04041000;Soro de leite modificado ou nao mesmo concentrado ou adicionado de acucar ou de outros edulcorantes;SIM;N/A;Anexo 1-A Secao XVII
04049000;Produtos constituidos por componentes naturais do leite nao especificados nem compreendidos noutras posicoes;SIM;N/A;Anexo 1-A Secao XVII
04051000;Manteiga;SIM;N/A;Anexo 1-A Secao XVII
04052000;Pasta de espalhar barrar de produtos provenientes do leite;SIM;N/A;Anexo 1-A Secao XVII
04059010;Oleo butirico de manteiga butter oil;SIM;N/A;Anexo 1-A Secao XVII
04059090;Outras materias gordas provenientes do leite;SIM;N/A;Anexo 1-A Secao XVII
04061010;Mozarela;SIM;N/A;Anexo 1-A Secao XVII
04061090;Outros queijos frescos nao curados incluindo o queijo de soro de leite e o requeijao;SIM;N/A;Anexo 1-A Secao XVII
04062000;Queijos ralados ou em po de qualquer tipo;SIM;N/A;Anexo 1-A Secao XVII
04063000;Queijos fundidos exceto ralados ou em po;SIM;N/A;Anexo 1-A Secao XVII
04064000;Queijos de pasta mofada azul e outros queijos que apresentem veios obtidos utilizando Penicillium roqueforti;SIM;N/A;Anexo 1-A Secao XVII
04069010;Outros queijos com um teor de umidade inferior a 36,0% em peso massa dura;SIM;N/A;Anexo 1-A Secao XVII
04069020;Outros queijos com um teor de umidade igual ou superior a 36,0% e inferior a 46,0% em peso massa semidura;SIM;N/A;Anexo 1-A Secao XVII
04069030;Outros queijos com um teor de umidade igual ou superior a 46,0% e inferior a 55,0% em peso massa macia;SIM;N/A;Anexo 1-A Secao XVII
04069090;Outros queijos;SIM;N/A;Anexo 1-A Secao XVII
09012100;Cafe torrado nao descafeinado;SIM;N/A;Anexo 1-A Secao XVII
09012200;Cafe torrado descafeinado;SIM;N/A;Anexo 1-A Secao XVII
09019000;Outros cafe mesmo torrado ou descafeinado cascas e peliculas de cafe sucedaneos do cafe que contenham cafe em qualquer proporcao;SIM;N/A;Anexo 1-A Secao XVII
15079011;Oleo de soja refinado em recipientes com capacidade inferior ou igual a 5 l;SIM;N/A;Anexo 1-A Secao XVII
15089000;Outros oleos de amendoim e respectivas fracoes mesmo refinados mas nao quimicamente modificados;SIM;N/A;Anexo 1-A Secao XVII
15092000;Azeite de oliva oliveira extra virgem;SIM;N/A;Anexo 1-A Secao XVII
15093000;Azeite de oliva oliveira virgem;SIM;N/A;Anexo 1-A Secao XVII
15094000;Outros azeites de oliva oliveira virgens;SIM;N/A;Anexo 1-A Secao XVII
15099010;Azeite de oliva refinado;SIM;N/A;Anexo 1-A Secao XVII
15099090;Outros azeites de oliva oliveira e respectivas fracoes;SIM;N/A;Anexo 1-A Secao XVII
15101000;Oleo de bagaco de azeitona em bruto;SIM;N/A;Anexo 1-A Secao XVII
15109000;Outros oleos e respectivas fracoes obtidos exclusivamente a partir de azeitonas;SIM;N/A;Anexo 1-A Secao XVII
15121911;Oleo de girassol refinado em recipientes com capacidade inferior ou igual a 5 l;SIM;N/A;Anexo 1-A Secao XVII
15122910;Oleo de algodao refinado;SIM;N/A;Anexo 1-A Secao XVII
15131900;Outros oleos de coco copra e respectivas fracoes;SIM;N/A;Anexo 1-A Secao XVII
15132911;Oleo de cocombocaya Acrocomia totai;SIM;N/A;Anexo 1-A Secao XVII
15132919;Outros oleos de amendoa de palma palmiste coconote;SIM;N/A;Anexo 1-A Secao XVII
15132920;Oleo de babacu;SIM;N/A;Anexo 1-A Secao XVII
15141910;Oleos de nabo silvestre ou de colza com baixo teor de acido erucico refinados;SIM;N/A;Anexo 1-A Secao XVII
15149910;Outros oleos de nabo silvestre de colza ou de mostarda refinados;SIM;N/A;Anexo 1-A Secao XVII
15151900;Outros oleos de linhaca sementes de linho e respectivas fracoes;SIM;N/A;Anexo 1-A Secao XVII
15152910;Oleo de milho refinado em recipientes com capacidade inferior ou igual a 5 l;SIM;N/A;Anexo 1-A Secao XVII
15152990;Outros oleos de milho e respectivas fracoes;SIM;N/A;Anexo 1-A Secao XVII
15153000;Oleo de ricino mamona e respectivas fracoes;SIM;N/A;Anexo 1-A Secao XVII
15155000;Oleo de gergelim sesamo e respectivas fracoes;SIM;N/A;Anexo 1-A Secao XVII
15159010;Oleo de jojoba e respectivas fracoes;SIM;N/A;Anexo 1-A Secao XVII
15159022;Oleo de tungue refinado;SIM;N/A;Anexo 1-A Secao XVII
15159090;Outras gorduras e oleos vegetais ou de origem microbiana e respectivas fracoes fixos mesmo refinados mas nao quimicamente modificados;SIM;N/A;Anexo 1-A Secao XVII
15162000;Gorduras e oleos vegetais e respectivas fracoes;SIM;N/A;Anexo 1-A Secao XVII
15171000;Margarina exceto a margarina liquida;SIM;N/A;Anexo 1-A Secao XVII
15179010;Misturas de oleos refinados em recipientes com capacidade inferior ou igual a 5 l;SIM;N/A;Anexo 1-A Secao XVII
15179090;Outras misturas ou preparacoes alimenticias de gorduras ou de oleos vegetais;SIM;N/A;Anexo 1-A Secao XVII
20089100;Palmitos;SIM;N/A;Anexo 1-A Secao XVII
20091100;Suco sumo de laranja congelado;SIM;N/A;Anexo 1-A Secao XVII
20091200;Suco sumo de laranja nao congelado com valor Brix nao superior a 20;SIM;N/A;Anexo 1-A Secao XVII
20091900;Outros sucos sumos de laranja;SIM;N/A;Anexo 1-A Secao XVII
20092100;Suco sumo de toranja suco sumo de pomelo com valor Brix nao superior a 20;SIM;N/A;Anexo 1-A Secao XVII
20092900;Outros sucos sumos de toranja ou de pomelo;SIM;N/A;Anexo 1-A Secao XVII
20093100;Suco sumo de qualquer outro citrico com valor Brix nao superior a 20;SIM;N/A;Anexo 1-A Secao XVII
20093900;Outros sucos sumos de qualquer outro citrico;SIM;N/A;Anexo 1-A Secao XVII
20094100;Suco sumo de abacaxi ananas com valor Brix nao superior a 20;SIM;N/A;Anexo 1-A Secao XVII
20094900;Outros sucos sumos de abacaxi ananas;SIM;N/A;Anexo 1-A Secao XVII
20095000;Suco sumo de tomate;SIM;N/A;Anexo 1-A Secao XVII
20096100;Suco sumo de uva incluindo os mostos de uvas com valor Brix nao superior a 30;SIM;N/A;Anexo 1-A Secao XVII
20096900;Outros sucos sumos de uva incluindo os mostos de uvas;SIM;N/A;Anexo 1-A Secao XVII
20097100;Suco sumo de maca com valor Brix nao superior a 20;SIM;N/A;Anexo 1-A Secao XVII
20097900;Outros sucos sumos de maca;SIM;N/A;Anexo 1-A Secao XVII
20098100;Suco sumo de arando vermelho cranberries Vaccinium macrocarpon Vaccinium oxycoccos airela vermelha Vaccinium vitis-idaea;SIM;N/A;Anexo 1-A Secao XVII
20098911;Suco sumo de caju;SIM;N/A;Anexo 1-A Secao XVII
20098912;Suco sumo de maracuja;SIM;N/A;Anexo 1-A Secao XVII
20098913;Suco sumo de manga;SIM;N/A;Anexo 1-A Secao XVII
20098919;Outros sucos sumos de uma unica fruta;SIM;N/A;Anexo 1-A Secao XVII
20098921;Agua de coco;SIM;N/A;Anexo 1-A Secao XVII
20098922;Suco sumo de acerola;SIM;N/A;Anexo 1-A Secao XVII
20098990;Outros sucos sumos de fruta ou de produtos horticulas;SIM;N/A;Anexo 1-A Secao XVII
20099000;Misturas de sucos sumos;SIM;N/A;Anexo 1-A Secao XVII
21069010;Xarope ou extrato concentrado destinados ao preparo de refrigerante em maquina pre-mix ou post-mix;SIM;N/A;Anexo 1-A Secao IV
21069010;Capsula de refrigerante;SIM;N/A;Anexo 1-A Secao IV
21069090;Bebidas energeticas;SIM;N/A;Anexo 1-A Secao IV
21069090;Bebidas hidroeletroliticas;SIM;N/A;Anexo 1-A Secao IV
22021000;Agua aromatizada artificialmente exceto os refrescos e refrigerantes;SIM;N/A;Anexo 1-A Secao IV
22021000;Refrigerante;SIM;N/A;Anexo 1-A Secao IV
22029100;Cerveja sem alcool;SIM;N/A;Anexo 1-A Secao IV
22029900;Outras aguas minerais gasosa ou nao ou potavel naturais inclusive gaseificadas ou aromatizadas artificialmente exceto os refrescos e refrigerantes;SIM;N/A;Anexo 1-A Secao IV
22029900;Refrigerante;SIM;N/A;Anexo 1-A Secao IV
22029900;Bebidas energeticas;SIM;N/A;Anexo 1-A Secao IV
22029900;Bebidas hidroeletroliticas;SIM;N/A;Anexo 1-A Secao IV
22030000;Cervejas de malte;SIM;N/A;Anexo 1-A Secao IV
22030000;Chope;SIM;N/A;Anexo 1-A Secao IV
22051000;Vermutes e outros vinhos de uvas frescas aromatizados por plantas ou substancias aromaticas em recipientes de capacidade nao superior a 2 l;SIM;N/A;Anexo 1-A Secao III-A
22059000;Outros vermutes e vinhos de uvas frescas aromatizados por plantas ou substancias aromaticas;SIM;N/A;Anexo 1-A Secao III-A
22060010;Sidra;SIM;N/A;Anexo 1-A Secao III-A
22060090;Outras bebidas fermentadas por exemplo perada hidromel saque misturas de bebidas fermentadas e misturas de bebidas fermentadas com bebidas nao alcoolicas;SIM;N/A;Anexo 1-A Secao III-A
22071010;Alcool etilico nao desnaturado com um teor de agua inferior ou igual a 1% vol;SIM;N/A;Anexo 1-A Secao III-A
22071090;Outros alcoois etilicos nao desnaturados com um teor alcoolico em volume igual ou superior a 80% vol;SIM;N/A;Anexo 1-A Secao III-A
22072011;Alcool etilico desnaturado com um teor de agua inferior ou igual a 1% vol;SIM;N/A;Anexo 1-A Secao III-A
22072019;Outros alcoois etilicos desnaturados;SIM;N/A;Anexo 1-A Secao III-A
22072020;Aguardente desnaturada;SIM;N/A;Anexo 1-A Secao III-A
22082000;Aguardentes de vinho ou de bagaco de uvas;SIM;N/A;Anexo 1-A Secao III-A
22083010;Uisques com um teor alcoolico em volume superior a 50% vol em recipientes de capacidade igual ou superior a 50 l;SIM;N/A;Anexo 1-A Secao III-A
22083020;Uisques em embalagens de capacidade inferior ou igual a 2 l;SIM;N/A;Anexo 1-A Secao III-A
22083090;Outros uisques;SIM;N/A;Anexo 1-A Secao III-A
22084000;Rum e outras aguardentes provenientes da destilacao apos fermentacao de produtos da cana-de-acucar;SIM;N/A;Anexo 1-A Secao III-A
22085000;Gim e genebra;SIM;N/A;Anexo 1-A Secao III-A
22086000;Vodca;SIM;N/A;Anexo 1-A Secao III-A
22087000;Licores;SIM;N/A;Anexo 1-A Secao III-A
22089000;Outros alcoois etilicos nao desnaturados com um teor alcoolico em volume inferior a 80% vol aguardentes licores e outras bebidas espirituosas;SIM;N/A;Anexo 1-A Secao III-A
23091000;Alimentos para caes ou gatos acondicionados para venda a retalho;SIM;N/A;Anexo 1-A Secao XXI
23099010;Alimentos para caes ou gatos acondicionados para venda a retalho;SIM;N/A;Anexo 1-A Secao XXI
23099030;Bolachas e biscoitos;SIM;N/A;Anexo 1-A Secao XXI
23099060;Alimentos para caes ou gatos acondicionados para venda a retalho;SIM;N/A;Anexo 1-A Secao XXI
23099090;Outras preparacoes do tipo utilizado na alimentacao de animais;SIM;N/A;Anexo 1-A Secao XXI
24021000;Charutos e cigarrilhas que contenham tabaco;SIM;N/A;Anexo 1-A Secao V
24022000;Cigarros que contenham tabaco;SIM;N/A;Anexo 1-A Secao V
24029000;Outros charutos cigarrilhas e cigarros de tabaco ou dos seus sucedaneos;SIM;N/A;Anexo 1-A Secao V
24031100;Tabaco para narguile cachimbo de agua mencionado na Nota de subposicao 1 do presente Capitulo;SIM;N/A;Anexo 1-A Secao V
24031900;Outros tabacos para fumar mesmo que contenha sucedaneos do tabaco em qualquer proporcao;SIM;N/A;Anexo 1-A Secao V
25231000;Cimentos nao pulverizados denominados clinkers;SIM;N/A;Anexo 1-A Secao VI
25232100;Cimentos Portland brancos mesmo corados artificialmente;SIM;N/A;Anexo 1-A Secao VI
25232910;Cimento Portland comum;SIM;N/A;Anexo 1-A Secao VI
25232990;Outros cimentos Portland;SIM;N/A;Anexo 1-A Secao VI
25233000;Cimentos aluminosos;SIM;N/A;Anexo 1-A Secao VI
25239000;Outros cimentos hidraulicos;SIM;N/A;Anexo 1-A Secao VI
40111000;Pneumaticos novos de borracha do tipo utilizado em automoveis de passageiros incluindo os veiculos de uso misto station wagons e os automoveis de corrida;SIM;N/A;Anexo 1-A Secao XVI
40112010;Pneumaticos novos de borracha do tipo utilizado em onibus autocarros ou caminhoes de medida 11,00-24;SIM;N/A;Anexo 1-A Secao XVI
40112090;Outros pneumaticos novos de borracha do tipo utilizado em onibus autocarros ou caminhoes;SIM;N/A;Anexo 1-A Secao XVI
40114000;Pneumaticos novos de borracha do tipo utilizado em motocicletas;SIM;N/A;Anexo 1-A Secao XVI
40115000;Pneumaticos novos de borracha do tipo utilizado em bicicletas;SIM;N/A;Anexo 1-A Secao XVI
40117010;Pneumaticos novos de borracha do tipo utilizado em veiculos e maquinas agricolas ou florestais nas seguintes medidas 4,00-15 4,00-18 4,00-19 5,00-15 5,00-16 5,50-16 6,00-16 6,00-19 6,00-20 6,50-16 6,50-20 7,50-16 7,50-18 7,50-20;SIM;N/A;Anexo 1-A Secao XVI
40117090;Outros pneumaticos novos de borracha do tipo utilizado em veiculos e maquinas agricolas ou florestais;SIM;N/A;Anexo 1-A Secao XVI
40118010;Pneumaticos novos de borracha radiais para dumpers concebidos para serem utilizados fora de rodovias com secao de largura igual ou superior a 940 mm 37 para aros de diametro igual ou superior a 1448 mm 57;SIM;N/A;Anexo 1-A Secao XVI
40118020;Outros pneumaticos novos de borracha com secao de largura igual ou superior a 1143 mm 45 para aros de diametro igual ou superior a 1143 mm 45;SIM;N/A;Anexo 1-A Secao XVI
40118090;Outros pneumaticos novos de borracha do tipo utilizado em veiculos e maquinas para a construcao civil de mineracao e de manutencao industrial;SIM;N/A;Anexo 1-A Secao XVI
40119010;Pneumaticos novos de borracha com secao de largura igual ou superior a 1143 mm 45 para aros de diametro igual ou superior a 1143 mm 45;SIM;N/A;Anexo 1-A Secao XVI
40119090;Outros pneumaticos novos de borracha;SIM;N/A;Anexo 1-A Secao XVI
40121100;Pneumaticos recauchutados do tipo utilizado em automoveis de passageiros incluindo os veiculos de uso misto station wagons e os automoveis de corrida;SIM;N/A;Anexo 1-A Secao XVI
40121200;Pneumaticos recauchutados do tipo utilizado em onibus autocarros ou caminhoes;SIM;N/A;Anexo 1-A Secao XVI
40121900;Outros pneumaticos recauchutados;SIM;N/A;Anexo 1-A Secao XVI
40129010;Flaps de borracha;SIM;N/A;Anexo 1-A Secao XVI
40129090;Protetores de borracha;SIM;N/A;Anexo 1-A Secao XVI
40131010;Camaras de ar de borracha para pneumaticos do tipo utilizado em onibus ou caminhoes de medida 11,00-24;SIM;N/A;Anexo 1-A Secao XVI
40131090;Outras camaras de ar de borracha do tipo utilizado em automoveis de passageiros onibus ou caminhoes;SIM;N/A;Anexo 1-A Secao XVI
40132000;Camaras de ar de borracha do tipo utilizado em bicicletas;SIM;N/A;Anexo 1-A Secao XVI
40139000;Outras camaras de ar de borracha;SIM;N/A;Anexo 1-A Secao XVI
48030090;Outros papeis do tipo utilizado para papel higienico lencos toalhitas demaquilantes toalhas guardanapos ou para papel semelhante de uso domestico higienico ou toucador;SIM;N/A;Anexo 1-A Secao XV
48059100;Outro papel e cartao nao revestidos em rolos ou em folhas de peso igual ou superior a 150 g/m² mas inferior a 225 g/m²;SIM;N/A;Anexo 1-A Secao XVIII
48062000;Papel impermeavel a gordura;SIM;N/A;Anexo 1-A Secao XVIII
48081000;Papel e cartao ondulados canelados mesmo perfurados;SIM;N/A;Anexo 1-A Secao XVIII
48115122;De peso superior a 150 g/m² com um conteudo de fibras de madeira obtidas por processo mecanico superior a 50% branqueado com face superior lisa;SIM;N/A;Anexo 1-A Secao XVIII
48115923;Outros de peso superior a 150 g/m²;SIM;N/A;Anexo 1-A Secao XVIII
48181000;Papel higienico;SIM;N/A;Anexo 1-A Secao XIX
48182000;Lencos incluindo os demaquilantes e toalhas de mao;SIM;N/A;Anexo 1-A Secao XIX
48183000;Toalhas de mesa e guardanapos;SIM;N/A;Anexo 1-A Secao XIX
48189090;Outros artigos de uso domestico higienico ou de toucador de pasta de papel papel ouate de celulose ou mantas de fibras de celulose;SIM;N/A;Anexo 1-A Secao XIX
48201000;Livros de registro e de contabilidade blocos de notas de encomendas de recibos de apontamentos de papel para cartas memorandos agendas e artigos semelhantes;SIM;N/A;Anexo 1-A Secao XVIII
48202000;Cadernos;SIM;N/A;Anexo 1-A Secao XVIII
48203000;Classificadores pastas para documentos capas para processos e capas de folhas moveis;SIM;N/A;Anexo 1-A Secao XVIII
48204000;Formularios em blocos de papel multiplo mesmo com folhas intercaladas de papel-carbono papel quimico;SIM;N/A;Anexo 1-A Secao XVIII
48205000;Albuns para amostras ou para colecoes;SIM;N/A;Anexo 1-A Secao XVIII
48209000;Outros artigos escolares de escritorio ou de papelaria;SIM;N/A;Anexo 1-A Secao XVIII
48211000;Etiquetas de papel ou cartao impressas;SIM;N/A;Anexo 1-A Secao XVIII
48219000;Outras etiquetas de papel ou cartao;SIM;N/A;Anexo 1-A Secao XVIII
4823209;Outros filtros de papel e cartao;SIM;N/A;Anexo 1-A Secao XVIII
48236;Bandejas travessas pratos copos e artigos semelhantes de papel ou cartao;SIM;N/A;Anexo 1-A Secao XVIII
48237000;Artigos moldados ou prensados de pasta de papel;SIM;N/A;Anexo 1-A Secao XVIII
4823909;Outros artigos de pasta de papel papel cartao ouate de celulose ou mantas de fibras de celulose;SIM;N/A;Anexo 1-A Secao XVIII
70091000;Espelhos retrovisores para veiculos;SIM;N/A;Anexo 1-A Secao II
7013;Objetos de vidro para servico de mesa cozinha toucador escritorio ornamentacao de interiores ou usos semelhantes exceto os das posicoes 7010 ou 7018;SIM;N/A;Anexo 1-A Secao XV
8211;Facas de laminas cortantes ou serrilhadas incluindo as podadeiras exceto as da posicao 8208 e suas laminas;SIM;N/A;Anexo 1-A Secao IX
82130000;Tesouras e suas laminas;SIM;N/A;Anexo 1-A Secao IX
8214;Outros artigos de cutelaria por exemplo maquinas de cortar o cabelo ou tosquiar maquinas de picar carne fendeleiras cutelos de acougue ou de cozinha espalmadeiras;SIM;N/A;Anexo 1-A Secao IX
8215;Colheres garfos conchas escumadeiras pas para tortas facas especiais para peixe ou para manteiga pincas para acucar e objetos semelhantes;SIM;N/A;Anexo 1-A Secao IX
83021000;Dobradicas de qualquer tipo incluindo os gonzos e charneiras;SIM;N/A;Anexo 1-A Secao XI
83024100;Outras guarnicoes artigos de ferragem e artigos semelhantes para edificios;SIM;N/A;Anexo 1-A Secao XI
83024200;Outras guarnicoes artigos de ferragem e artigos semelhantes para moveis;SIM;N/A;Anexo 1-A Secao XI
83024900;Outras guarnicoes artigos de ferragem e artigos semelhantes;SIM;N/A;Anexo 1-A Secao XI
83025000;Pateras cabides chapeleiras e artigos semelhantes;SIM;N/A;Anexo 1-A Secao XI
83026000;Fechos automaticos para portas;SIM;N/A;Anexo 1-A Secao XI
83081000;Grampos de fio curvado;SIM;N/A;Anexo 1-A Secao IX
83082000;Rebites tubulares ou de haste fendida;SIM;N/A;Anexo 1-A Secao IX
830890;Outras obras de metais comuns incluindo as partes;SIM;N/A;Anexo 1-A Secao IX
841510;Maquinas e aparelhos de ar-condicionado do tipo concebido para ser fixado numa janela parede teto ou piso pavimento formando um corpo unico ou do tipo split-system sistema com elementos separados;SIM;N/A;Anexo 1-A Secao XX
841582;Outras maquinas e aparelhos de ar-condicionado com dispositivo de refrigeracao;SIM;N/A;Anexo 1-A Secao XX
84181000;Combinacoes de refrigeradores e congeladores freezers munidos de portas ou gavetas exteriores separadas ou de uma combinacao desses elementos;SIM;N/A;Anexo 1-A Secao XX
84182100;Refrigeradores do tipo domestico de compressao;SIM;N/A;Anexo 1-A Secao XX
84182900;Outros refrigeradores do tipo domestico;SIM;N/A;Anexo 1-A Secao XX
84183000;Congeladores freezers horizontais arcas de capacidade nao superior a 800 l;SIM;N/A;Anexo 1-A Secao XX
84184000;Congeladores freezers verticais de capacidade nao superior a 900 l;SIM;N/A;Anexo 1-A Secao XX
841850;Outros moveis arcas armarios vitrines balcoes e moveis semelhantes para a conservacao e exposicao de produtos que incorporem um equipamento para a producao de frio;SIM;N/A;Anexo 1-A Secao XX
8418699;Outros materiais maquinas e aparelhos para a producao de frio;SIM;N/A;Anexo 1-A Secao XX
842112;Secadores de roupa;SIM;N/A;Anexo 1-A Secao XX
84212100;Aparelhos para filtrar ou depurar agua;SIM;N/A;Anexo 1-A Secao XX
842211;Maquinas de lavar louca do tipo domestico;SIM;N/A;Anexo 1-A Secao XX
84221900;Outras maquinas de lavar louca;SIM;N/A;Anexo 1-A Secao XX
844331;Maquinas que executem pelo menos duas das seguintes funcoes impressao copia ou transmissao de telecopia fax capazes de ser conectadas a uma maquina automatica para processamento de dados ou a uma rede;SIM;N/A;Anexo 1-A Secao XX
844332;Outras impressoras aparelhos de copiar e aparelhos de telecopiar fax mesmo combinados entre si capazes de ser conectadas a uma maquina automatica para processamento de dados ou a uma rede;SIM;N/A;Anexo 1-A Secao XX
845011;Maquinas de lavar roupa de uso domestico inteiramente automaticas de capacidade nao superior a 10 kg em peso de roupa seca;SIM;N/A;Anexo 1-A Secao XX
845012;Outras maquinas de lavar roupa de uso domestico com secador centrifugo incorporado de capacidade nao superior a 10 kg em peso de roupa seca;SIM;N/A;Anexo 1-A Secao XX
845019;Outras maquinas de lavar roupa de uso domestico de capacidade nao superior a 10 kg em peso de roupa seca;SIM;N/A;Anexo 1-A Secao XX
845020;Maquinas de lavar roupa de uso domestico de capacidade superior a 10 kg em peso de roupa seca;SIM;N/A;Anexo 1-A Secao XX
845121;Maquinas de secar de uso domestico de capacidade nao superior a 10 kg em peso de roupa seca;SIM;N/A;Anexo 1-A Secao XX
845129;Outras maquinas de secar de uso domestico;SIM;N/A;Anexo 1-A Secao XX
847130;Maquinas automaticas para processamento de dados portateis de peso nao superior a 10 kg que contenham pelo menos uma unidade central de processamento um teclado e uma tela ecra;SIM;N/A;Anexo 1-A Secao XX
84714;Outras maquinas automaticas para processamento de dados;SIM;N/A;Anexo 1-A Secao XX
847150;Unidades de processamento exceto as das subposicoes 847141 ou 847149 podendo conter no mesmo corpo um ou dois dos seguintes tipos de unidades unidade de memoria unidade de entrada e unidade de saida;SIM;N/A;Anexo 1-A Secao XX
847160;Unidades de entrada ou de saida podendo conter no mesmo corpo unidades de memoria;SIM;N/A;Anexo 1-A Secao XX
847170;Unidades de memoria;SIM;N/A;Anexo 1-A Secao XX
847190;Outras unidades de maquinas automaticas para processamento de dados;SIM;N/A;Anexo 1-A Secao XX
85043;Outros transformadores de potencia nao superior a 16 kVA;SIM;N/A;Anexo 1-A Secao XX
850440;Conversores estaticos;SIM;N/A;Anexo 1-A Secao XX
8506;Pilhas e baterias de pilhas eletricas;SIM;N/A;Anexo 1-A Secao XX
8507;Acumuladores eletricos incluindo os seus separadores mesmo de forma quadrada ou retangular;SIM;N/A;Anexo 1-A Secao XX
8508;Aspiradores;SIM;N/A;Anexo 1-A Secao XX
8509;Aparelhos eletromecanicos de motor eletrico incorporado de uso domestico exceto os aspiradores da posicao 8508;SIM;N/A;Anexo 1-A Secao XX
8510;Aparelhos ou maquinas de barbear maquinas de cortar o cabelo ou de tosquiar e aparelhos de depilar com motor eletrico incorporado;SIM;N/A;Anexo 1-A Secao XX
8513;Lanternas eletricas portateis destinadas a funcionar por meio de sua propria fonte de energia por exemplo de pilhas de acumuladores de magnetos exceto os aparelhos de iluminacao da posicao 8512;SIM;N/A;Anexo 1-A Secao XX
85161000;Aquecedores eletricos de agua incluindo os de imersao;SIM;N/A;Anexo 1-A Secao XX
85162;Aparelhos eletricos para aquecimento de ambientes do solo ou para usos semelhantes;SIM;N/A;Anexo 1-A Secao XX
85163;Aparelhos eletrotermicos para arranjos do cabelo ou para secar as maos;SIM;N/A;Anexo 1-A Secao XX
85164000;Ferros eletricos de passar;SIM;N/A;Anexo 1-A Secao XX
85165000;Fornos de micro-ondas;SIM;N/A;Anexo 1-A Secao XX
85166000;Outros fornos fogoes de cozinha fogareiros incluindo as chapas de coccao grelhas e assadeiras;SIM;N/A;Anexo 1-A Secao XX
85167;Outros aparelhos eletrotermicos;SIM;N/A;Anexo 1-A Secao XX
85171100;Aparelhos telefonicos por fio com unidade auscultador-microfone sem fio;SIM;N/A;Anexo 1-A Secao XX
85171300;Smartphones e outros telefones para redes celulares ou para outras redes sem fio;SIM;N/A;Anexo 1-A Secao XX
851714;Outros telefones para redes celulares ou para outras redes sem fio;SIM;N/A;Anexo 1-A Secao XX
851718;Outros aparelhos telefonicos;SIM;N/A;Anexo 1-A Secao XX
851762;Aparelhos para recepcao conversao transmissao e regeneracao de voz imagens ou outros dados incluindo os aparelhos de comutacao e roteamento;SIM;N/A;Anexo 1-A Secao XX
8518;Microfones e seus suportes alto-falantes mesmo montados nas suas caixas acusticas fones de ouvido mesmo combinados com um microfone e conjuntos ou sortidos constituidos por um microfone e um ou mais alto-falantes amplificadores eletricos de audiofrequencia aparelhos eletricos de amplificacao de som;SIM;N/A;Anexo 1-A Secao XX
8519;Aparelhos de gravacao de som aparelhos de reproducao de som aparelhos de gravacao e de reproducao de som;SIM;N/A;Anexo 1-A Secao XX
8521;Aparelhos de gravacao ou de reproducao de video mesmo com um receptor de sinais de video incorporado;SIM;N/A;Anexo 1-A Secao XX
8522;Partes e acessorios reconheciveis como sendo exclusiva ou principalmente destinados aos aparelhos das posicoes 8519 a 8521;SIM;N/A;Anexo 1-A Secao XX
852589;Outras cameras de televisao cameras de video de imagens fixas e outras cameras de video;SIM;N/A;Anexo 1-A Secao XX
8527;Aparelhos receptores para radiodifusao mesmo combinados num mesmo involucro com um aparelho de gravacao ou de reproducao de som ou com um relogio;SIM;N/A;Anexo 1-A Secao XX
8528;Monitores e projetores que nao incorporem aparelho receptor de televisao aparelhos receptores de televisao mesmo que incorporem um aparelho receptor de radiodifusao ou um aparelho de gravacao ou de reproducao de som ou de imagens;SIM;N/A;Anexo 1-A Secao XX
8539;Lampadas e tubos eletricos de incandescencia ou de descarga incluindo os artigos denominados farois e projetores em unidades seladas e as lampadas e tubos de raios ultravioleta ou infravermelhos lampadas de arco lampadas e tubos de diodos emissores de luz LED;SIM;N/A;Anexo 1-A Secao X
8540;Lampadas tubos e valvulas eletronicas de catodo quente catodo frio ou fotocatodo por exemplo lampadas tubos e valvulas de vacuo de vapor ou de gas tubos retificadores de vapor de mercurio tubos catodicos tubos e valvulas para cameras de televisao;SIM;N/A;Anexo 1-A Secao X
8544;Fios cabos incluindo os cabos coaxiais e outros condutores isolados para usos eletricos mesmo com pecas de conexao fios de fibras opticas constituidos por fibras embainhadas individualmente mesmo com condutores eletricos ou munidos de pecas de conexao;SIM;N/A;Anexo 1-A Secao XIII
8702;Veiculos automoveis para transporte de 10 pessoas ou mais incluindo o motorista;SIM;N/A;Anexo 1-A Secao XXIV
8703;Automoveis de passageiros e outros veiculos automoveis principalmente concebidos para transporte de pessoas exceto os da posicao 8702 incluindo os veiculos de uso misto station wagons e os automoveis de corrida;SIM;N/A;Anexo 1-A Secao XXIV
8704;Veiculos automoveis para transporte de mercadorias;SIM;N/A;Anexo 1-A Secao XXIV
8705;Veiculos automoveis para usos especiais exceto os concebidos principalmente para transporte de pessoas ou de mercadorias por exemplo auto-socorros caminhoes-guindastes veiculos de combate a incendios caminhoes-betoneiras veiculos para varrer veiculos para espalhar veiculos-oficinas veiculos radiologicos;SIM;N/A;Anexo 1-A Secao XXIV
870600;Chassis com motor para veiculos automoveis das posicoes 8701 a 8705;SIM;N/A;Anexo 1-A Secao XXIV
8711;Motocicletas incluindo os ciclomotores e outros veiculos equipados com motor auxiliar mesmo com carro lateral carros laterais;SIM;N/A;Anexo 1-A Secao XXV
8716;Reboques e semirreboques para quaisquer veiculos outros veiculos nao autopropulsados e suas partes;SIM;N/A;Anexo 1-A Secao XXIV
9006;Cameras fotograficas aparelhos e dispositivos incluindo as lampadas e tubos de luz relampago flash para fotografia exceto as da posicao 8539;SIM;N/A;Anexo 1-A Secao XX
9007;Cameras e projetores cinematograficos mesmo com aparelhos de gravacao ou de reproducao de som incorporados;SIM;N/A;Anexo 1-A Secao XX
90189099;Outros instrumentos e aparelhos para medicina cirurgia odontologia e veterinaria;SIM;N/A;Anexo 1-A Secao XIV
90191000;Aparelhos de mecanoterapia aparelhos de massagem aparelhos de psicotecnica;SIM;N/A;Anexo 1-A Secao XIV
902000;Outros aparelhos respiratorios e mascaras contra gases exceto as mascaras de protecao desprovidas de mecanismo e de elemento filtrante amovivel;SIM;N/A;Anexo 1-A Secao XIV
9021;Artigos e aparelhos ortopedicos incluindo as cintas e fundas medico-cirurgicas e as muletas talas goteiras e outros artigos e aparelhos para fraturas artigos e aparelhos de protese aparelhos para facilitar a audicao dos surdos e outros aparelhos para compensar uma deficiencia ou uma incapacidade destinados a serem transportados a mao ou sobre as pessoas ou a serem implantados no organismo;SIM;N/A;Anexo 1-A Secao XIV
90328911;Reguladores de voltagem eletronicos;SIM;N/A;Anexo 1-A Secao XIII
9101;Relogios de pulso de bolso e semelhantes incluindo os contadores de tempo dos mesmos tipos com caixa de metais preciosos ou de metais folheados ou chapeados de metais preciosos plaque;SIM;N/A;Anexo 1-A Secao XXVI
9102;Relogios de pulso de bolso e semelhantes incluindo os contadores de tempo dos mesmos tipos exceto os da posicao 9101;SIM;N/A;Anexo 1-A Secao XXVI
9103;Despertadores e outros relogios com mecanismo de pequeno volume;SIM;N/A;Anexo 1-A Secao XXVI
9105;Despertadores outros relogios e aparelhos de relojoaria semelhantes exceto os com mecanismo de pequeno volume;SIM;N/A;Anexo 1-A Secao XXVI
9401;Assentos exceto os da posicao 9402 mesmo transformaveis em camas e suas partes;SIM;N/A;Anexo 1-A Secao XI
9403;Outros moveis e suas partes;SIM;N/A;Anexo 1-A Secao XI
9405;Luminarias e aparelhos de iluminacao incluindo os projetores e suas partes nao especificados nem compreendidos noutras posicoes anuncios cartazes ou tabuletas e placas indicadoras luminosos e artigos semelhantes com uma fonte de luz fixa permanente e suas partes nao especificadas nem compreendidas noutras posicoes;SIM;N/A;Anexo 1-A Secao XI
9504;Consoles e maquinas de jogos de video artigos para jogos de salao incluindo os jogos com motor ou outro mecanismo os bilhares as mesas especiais para jogos de cassino e os jogos de balizas automaticos boliches;SIM;N/A;Anexo 1-A Secao XX
9506;Artigos e equipamentos para cultura fisica ginasia atletismo outros esportes incluindo o tenis de mesa e o badminton ou para jogos ao ar livre nao especificados nem compreendidos noutras posicoes deste Capitulo piscinas incluindo as infantis;SIM;N/A;Anexo 1-A Secao XXVI
9603;Vassouras escovas mesmo as que sejam partes de maquinas de aparelhos ou de veiculos escovas mecanicas de uso manual nao motorizadas e espanadores pinceis e brochas exceto os da subposicao 960330 rolos para pintura bonecas e rolos para pintura preparacoes como escovas;SIM;N/A;Anexo 1-A Secao XII
96050000;Sortidos de viagem para toucador de pessoas para costura ou para limpeza de calcado ou de roupas;SIM;N/A;Anexo 1-A Secao XIX
9608;Canetas esferograficas canetas e marcadores com ponta de feltro ou com outras pontas porosas canetas-tinteiro tinteiros e outras canetas lapiseiras canetas porta-penas porta-lapis e artigos semelhantes partes incluindo as tampas e prendedores desses artigos exceto os da posicao 9609;SIM;N/A;Anexo 1-A Secao XVIII
9609;Lapis minas para lapis ou para lapiseiras pasteis e carvoes lapis de ardosa ou de greda e giz para escrever ou para desenhar;SIM;N/A;Anexo 1-A Secao XVIII
9613;Isqueiros e outros acendedores mesmo mecanicos ou eletricos e suas partes exceto pedras e pavios;SIM;N/A;Anexo 1-A Secao XXVI
96140000;Cachimbos incluindo os seus fornilhos e piteiras boquilhas para charutos ou cigarros e suas partes;SIM;N/A;Anexo 1-A Secao XXVI
9615;Pentes travessas para cabelo e artigos semelhantes grampos ganchos para cabelo alfinetes para cabelo pincas onduladores bobs e artigos semelhantes para penteados exceto os da posicao 8516 e suas partes;SIM;N/A;Anexo 1-A Secao XIX
9616;Vaporizadores de toucador e suas armacoes e cabecas de vaporizadores borlas e esponjas para po ou para aplicacao de outros cosmeticos ou de produtos de toucador;SIM;N/A;Anexo 1-A Secao XIX
961700;Garrafas termicas e outros recipientes isotermicos montados com isolamento a vacuo bem como suas partes exceto ampolas de vidro;SIM;N/A;Anexo 1-A Secao XX
9619;Absorventes higienicos externos e tampoes higienicos fraldas e cueiros para bebes e artigos higienicos semelhantes de qualquer materia;SIM;N/A;Anexo 1-A Secao XIX"


                    Com base EXCLUSIVAMENTE no contexto forneça um resumo detalhado e claro do tratamento tributário para o seguinte item: "${query}".

                    O resumo deve obrigatoriamente incluir os seguintes pontos, quando aplicáveis:

                    1.  **Alíquota Interna:** Qual a alíquota padrão de ICMS para este produto em operações dentro de SC? 
                    2.  **Substituição Tributária (ICMS-ST):** O produto está sujeito ao regime de ST? Se sim, mencione o MVA/IVA-ST aplicável (original e ajustado para 4% e 12%, se houver) e a base legal (dispositivo do RICMS/SC).
                    3.  **Isenção:** Existe alguma isenção de ICMS para este produto? Se sim, qual e sob quais condições? Citar a base legal.
                    4.  **Redução de Base de Cálculo:** Há alguma redução na base de cálculo do ICMS? Se sim, qual o percentual e as condições? Citar a base legal.
                    5.  **Crédito Presumido:** Existe algum benefício de crédito presumido? Se sim, qual o percentual e para qual tipo de empresa/operação se aplica? Citar a base legal.
                    6.  **Observações Importantes:** Qualquer outra informação relevante, como regimes especiais, diferimento, ou particularidades da operação. Citar a base legal.

                    Formate a resposta usando Markdown, com títulos claros para cada seção em negrito, destacado e com fonte maior (ex: ## Alíquota, ## Substituição Tributária).
                    Se a descrição for muito genérica, informe que não foi possível localizar uma tributação específica e peça mais detalhes.
                    Aja como um consultor tributário especialista em legislação catarinense.
					
				Seja extremamente detalhista e verifique as informações levantadas.
				Caso o produto náo seja encontrato no contexto ALÍQUOTA DEVE SER 17% e os demais campos devem ser preenchidos como "não possui tratamento diferenciado."
				No relatório deve constar a informação: "última atualização Base de Dados: 18/08/2025."
                `;

                const responseText = await callGeminiApi(prompt);
                showResult(responseText);

            } catch (err) {
                console.error("Erro ao buscar dados:", err);
                if (err.message === "API_KEY_MISSING") {
                    showError("Erro de configuração: A chave da API do Google não foi adicionada. Edite o arquivo HTML e insira sua chave.");
                } else {
                    showError("Falha na comunicação com o serviço de busca. Verifique sua conexão ou tente mais tarde.");
                }
            }
        }

        /**
         * Chama a API do Gemini com retentativa (exponential backoff)
         * @param {string} prompt O prompt a ser enviado
         * @returns {Promise<string>} O texto da resposta
         */
        async function callGeminiApi(prompt) {
            // =================================================================================
            // IMPORTANTE: Chave de API do Google AI Studio.
            // =================================================================================
            const apiKey = "AIzaSyAwr9NszWntg_sxgRVf_6qJhAYHDPYGoeA";

            if (apiKey === "SUA_CHAVE_API_AQUI") {
                throw new Error("API_KEY_MISSING");
            }

            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=${apiKey}`;
            
            const payload = {
                contents: [{
                    role: "user",
                    parts: [{ text: prompt }]
                }],
                generationConfig: {
                    temperature: 0.2,
                    topP: 0.9,
                }
            };
            
            let response;
            let retries = 3;
            let delay = 1000;

            for (let i = 0; i < retries; i++) {
                try {
                    response = await fetch(apiUrl, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });

                    if (response.ok) {
                        const result = await response.json();
                        if (result.candidates && result.candidates[0]?.content?.parts?.[0]) {
                            return result.candidates[0].content.parts[0].text;
                        } else {
                           throw new Error("Resposta da API inválida ou vazia.");
                        }
                    } else {
                        if (response.status === 429 && i < retries - 1) {
                            await new Promise(resolve => setTimeout(resolve, delay));
                            delay *= 2; 
                            continue; 
                        }
                        throw new Error(`Erro na API: ${response.status} ${response.statusText}`);
                    }
                } catch (error) {
                    console.error(`Tentativa ${i + 1} falhou:`, error);
                    if (i === retries - 1) throw error; 
                }
            }
        }

        /**
         * Mostra o estado de carregamento
         */
        function showLoading() {
            placeholder.classList.add('hidden');
            errorContainer.classList.add('hidden');
            resultContent.classList.add('hidden');
            resultContent.innerHTML = '';
            loader.classList.remove('hidden');
            loader.classList.add('flex');
            searchButton.disabled = true;
            searchButton.classList.add('opacity-50', 'cursor-not-allowed');
        }

        /**
         * Mostra o resultado da busca
         * @param {string} text O texto de resultado em Markdown
         */
        function showResult(text) {
            loader.classList.add('hidden');
            loader.classList.remove('flex');
            errorContainer.classList.add('hidden');
            
            resultContent.innerHTML = marked.parse(text);
            
            resultContent.classList.remove('hidden');
            placeholder.classList.add('hidden');
            searchButton.disabled = false;
            searchButton.classList.remove('opacity-50', 'cursor-not-allowed');
        }

        /**
         * Mostra uma mensagem de erro
         * @param {string} message A mensagem a ser exibida
         */
        function showError(message) {
            loader.classList.add('hidden');
            loader.classList.remove('flex');
            placeholder.classList.add('hidden');
            resultContent.classList.add('hidden');
            
            errorMessage.textContent = message;
            errorContainer.classList.remove('hidden');
            
            searchButton.disabled = false;
            searchButton.classList.remove('opacity-50', 'cursor-not-allowed');
        }

    </script>
</body>
</html>
