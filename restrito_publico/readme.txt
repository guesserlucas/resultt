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
