'use client'
export default function renderWords(wordLines: string[], inputWords: string) {
    let globalIndex = 0;
    return wordLines.map((line, lineIndex) => (
        <div key={lineIndex} className="relative w-full flex justify-left text-center mb-2">
            {line.split('').map((char, index) => {
                if (globalIndex >= inputWords.length) {
                    return (
                        <span key={index} className="text-gray-500 opacity-70">
                            {char === ' ' ? '\u00A0' : char}
                        </span>
                    );
                }
                const isCorrect = inputWords[globalIndex] === char;
                const isCurrent = globalIndex === inputWords.length - 1;
                globalIndex++;
                return (
                    <span
                        key={index}
                        className={isCorrect ? "text-white" : "text-red-500"}
                    >
                        {char === ' ' ? '\u00A0' : char}
                        {isCurrent && <div className='inline-block border-l border-white text-transparent absolute animate-pulse -translate-x-[1px]'>А</div>}
                    </span>
                );
            })}
        </div>
    ));
}