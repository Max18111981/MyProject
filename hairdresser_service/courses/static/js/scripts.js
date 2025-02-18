document.addEventListener('DOMContentLoaded', function () {
    console.log('Скрипт загружен');
    const videoContainers = document.querySelectorAll('.video-container');

    videoContainers.forEach(container => {
        const preview = container.querySelector('.video-preview');
        const thumbnail = container.querySelector('.video-thumbnail');

        container.addEventListener('mouseenter', () => {
            thumbnail.style.opacity = 0; // Скрываем превью
            preview.style.opacity = 1; // Показываем видео-превью
            preview.play(); // Запускаем превью
        });

        container.addEventListener('mouseleave', () => {
            thumbnail.style.opacity = 1; // Показываем превью
            preview.style.opacity = 0; // Скрываем видео-превью
            preview.pause(); // Останавливаем превью
            preview.currentTime = 0; // Сбрасываем время воспроизведения
        });
    });
});