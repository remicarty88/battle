document.addEventListener('DOMContentLoaded', () => {
    const battleArena = document.getElementById('battle-arena');

    // Пример обновления статуса боя
    function updateBattle() {
        // Вставьте код для получения данных с сервера и обновления
        battleArena.innerText = "Бой продолжается...";
    }

    setInterval(updateBattle, 3000); // Обновлять каждые 3 секунды
});
