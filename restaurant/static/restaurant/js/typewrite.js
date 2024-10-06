const div1 = document.querySelector('#div1');
const div2 = document.querySelector('#div2');
const text = 'This application was made by Ilya Vlasiuk, group KН-Н223.';
const text2 = 'Subject area - 12: Restaurant.'

function textTyping(element, text, i=0){
    element.textContent += text[i];

    if (i == text.length - 1) {
        return;
    }
    setTimeout(() => textTyping(element, text, i+1), 50);
}

textTyping(div1, text);
textTyping(div2, text2);