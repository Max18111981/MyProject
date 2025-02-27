document.addEventListener('DOMContentLoaded', function () {
    console.log('Скрипт загружен');
    const videoContainers = document.querySelectorAll('.video-container');

    videoContainers.forEach(container => {
        const preview = container.querySelector('.video-preview');
        // const thumbnail = container.querySelector('.thumbnail-image');
        const playButton = container.querySelector('.play-button')

        container.addEventListener('mouseenter', () => {
            // thumbnail.style.opacity = 0; // Скрываем превью
            // preview.style.opacity = 1; // Показываем видео-превью
            playButton.style.opacity = 0;
            preview.play(); // Запускаем превью
        });

        container.addEventListener('mouseleave', () => {
            // thumbnail.style.opacity = 1; // Показываем превью
            // preview.style.opacity = 0; // Скрываем видео-превью
            playButton.style.opacity = 1;
            preview.pause(); // Останавливаем превью
            // preview.currentTime = 0; // Сбрасываем время воспроизведения
        });
    });
});


// Отключение правой кнопки мыши
document.addEventListener('contextmenu', function(event) {
    event.preventDefault();
});

// Запрет выделения текста
document.addEventListener('selectstart', function(event) {
    event.preventDefault();
});

// Запрет копирования (Ctrl+C)
document.addEventListener('copy', function(event) {
    event.preventDefault();
});


let duration = 0.8;
let delay = 0.3;
let revealText = document.querySelector(".reveal");
let letters = revealText.textContent.split("");
revealText.textContent = "";
let middle = letters.filter(e => e !== " ").length / 2;
letters.forEach((letter, i) => {
  let span = document.createElement("span");
  span.textContent = letter;
  span.style.animationDelay = `${delay + Math.abs(i - middle) * 0.1}s`;
  revealText.append(span);
});