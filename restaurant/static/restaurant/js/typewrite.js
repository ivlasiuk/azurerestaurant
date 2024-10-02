const div = document.querySelector('.text');
const text = 'This application was made by Ilya Vlasiuk, group KН-Н223.';

function textTyping(element, text, i=0){
    element.textContent += text[i];

    if (i == text.length - 1) {
        return;
    }
    setTimeout(() => textTyping(element, text, i+1), 50);
}

textTyping(div, text);