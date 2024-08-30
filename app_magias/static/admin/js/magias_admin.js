document.addEventListener('DOMContentLoaded', function() {
    const componentMCheckbox = document.querySelector('input[name="componentes"][value="M"]');
    const materialDescricaoField = document.querySelector('textarea[name="material_descricao"]');

    if (componentMCheckbox) {
        componentMCheckbox.addEventListener('change', function() {
            if (this.checked) {
                materialDescricaoField.style.display = 'block';  // Mostra o campo
            } else {
                materialDescricaoField.style.display = 'none';   // Esconde o campo
                materialDescricaoField.value = '';               // Limpa o valor
            }
        });

        // Verifica o estado inicial para mostrar/esconder o campo
        if (componentMCheckbox.checked) {
            materialDescricaoField.style.display = 'block';
        }
    }
});
