document.addEventListener("DOMContentLoaded", () => {
    const themeToggleDark = document.getElementById("dark-mode-toggle");
    const themeToggleLight = document.getElementById("light-mode-toggle");
    const body = document.body;

    // Função para aplicar o tema
    function applyTheme(theme) {
        body.setAttribute("data-bs-theme", theme);
        localStorage.setItem("theme", theme);
    }

    // Carregar tema preferido do armazenamento local
    const savedTheme = localStorage.getItem("theme") || 'light';
    applyTheme(savedTheme);

    // Configurar eventos de clique
    themeToggleDark.addEventListener("click", () => {
        applyTheme("dark");
        themeToggleDark.classList.add("active");
        themeToggleLight.classList.remove("active");
    });

    themeToggleLight.addEventListener("click", () => {
        applyTheme("light");
        themeToggleLight.classList.add("active");
        themeToggleDark.classList.remove("active");
    });
});
