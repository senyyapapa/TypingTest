export default function splitWords(words:string, maxLength: number) {
    const wordsArray = words.split(' ');
    const lines = [];
    let currentLine = '';

    wordsArray.forEach(word => {
        if ((currentLine + word).length <= maxLength)
        {
            currentLine += (currentLine ? ' ' : '') + word;
        } else {
            lines.push(currentLine + ' ');
            currentLine = word;
        }
    });

    if (currentLine) {lines.push(currentLine)}
    return lines;
}