$(document).ready(function() {
    // Exemplo de validação simples para garantir que todos os campos obrigatórios estejam preenchidos
    $("form").submit(function(event) {
        var isValid = true;

        // Verifica se todos os campos obrigatórios estão preenchidos
        $("form input[required]").each(function() {
            if ($(this).val() === "") {
                isValid = false;
                $(this).css("border", "1px solid red");  // Destaca campos não preenchidos
                $(this).next(".error-message").remove();
                $(this).after('<span class="error-message" style="color: red;">Este campo é obrigatório</span>');
            } else {
                $(this).css("border", "1px solid green");  // Marca campos válidos
                $(this).next(".error-message").remove();  // Remove a mensagem de erro
            }
        });

        // Impede o envio do formulário se algum campo estiver inválido
        if (!isValid) {
            event.preventDefault();  // Impede o envio do formulário
            alert("Por favor, preencha todos os campos obrigatórios.");
        }
    });

    // Exemplo de um campo de CPF com máscara
    $(".cpf").on("input", function() {
        var value = $(this).val().replace(/\D/g, "");  // Remove caracteres não numéricos
        if (value.length <= 11) {
            value = value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
        }
        $(this).val(value);
    });
});
