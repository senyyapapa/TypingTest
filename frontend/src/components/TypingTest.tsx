'use client';

import {useEffect, useState} from 'react';
import {RotateCcw} from "lucide-react";
import splitWords from "@/components/SplitWords";
import renderWords from "@/components/RenderWords";
import axios from 'axios';

const TypingPractice = () => {
    const [correctCount, setCorrectCount] = useState(0);
    const [inputWords, setInputWords] = useState('');
    const [timeLeft, setTimeLeft] = useState(15);
    const [finalRes, setFinalRes] = useState(0);
    const [timeStarted, setTimesStarted] = useState(false);
    const [testCompleted, setTestCompleted] = useState(false);
    const [accuracy, setAccuracy] = useState(0);
    const [initialTime, setInitialTime] = useState(15);
    const [words, setWords] = useState('');
    const [loading, setLoading]= useState(false);

    // const words = 'apple banana show sure the beautiful sunny sunshine origami planet word';
    const maxLength = 80;
    const wordsLine = splitWords(words, maxLength);

    async function fetchWords() {
        setLoading(true);
        const response = await axios.get('http://localhost:8000/api/users/get_words/words');
        const wordBackend: string = await response.data.words.join(' ');

        setWords(wordBackend);
        setLoading(false);
    }

    useEffect(() => {
       if (words === '') {fetchWords()}
    }, [words]);

    let count = 0;
    useEffect(() => {
        let interval: any;
        if (timeStarted && !testCompleted) {
            interval = setInterval(() => {
                setTimeLeft(prevTime => {
                    if (prevTime <= 1) {
                        clearInterval(interval);
                        setTestCompleted(true);
                        calculateRes(initialTime - timeLeft);
                        return 0;
                    }
                    return prevTime - 1;
                });
            }, 1000);
        }
        return () => clearInterval(interval);
    }, [timeStarted, testCompleted]);

    useEffect(() => {
        words.split('').forEach((char, index) => {
            if (index < inputWords.length && inputWords[index] === char) {
                count++;
            }
        });

        setCorrectCount(count);

        if (inputWords.length === 1 && !timeStarted) {
            setTimesStarted(true);
        }

        if (inputWords.length === words.length && !testCompleted && loading) {
            setTestCompleted(true);
            calculateRes(initialTime - timeLeft);
        }
    }, [inputWords, words, timeLeft, testCompleted, timeStarted]);

    const calculateRes = (timeSpent: number) => {
        const minuteSpent = timeSpent / 60;
        const wordCount = correctCount / 5;
        const wpm = minuteSpent > 0 ? wordCount / minuteSpent : 0;
        const testAccuracy = correctCount * 100 / inputWords.length;
        setFinalRes(wpm);
        setAccuracy(testAccuracy);
    }

    useEffect(() => {
        if (testCompleted) {
            calculateRes(initialTime - timeLeft);
        }
    }, [testCompleted]);

    const handleInput = (e: any) => {
        if (!testCompleted) {
            setInputWords(e.target.value);
        }
    };

    const testReset = (time: number) => {
        setCorrectCount(0);
        setTestCompleted(false);
        setInputWords('');
        setTimesStarted(false);
        setFinalRes(0);
        setWords('');
        if (time) {
            setInitialTime(time);
            setTimeLeft(time);
        } else {
            setTimeLeft(initialTime);
        }
    }

    const changeTime = (time: number) => {
        testReset(time);
    }

    return (
        <div className="flex flex-col items-center justify-center h-screen overflow-hidden bg-custom-gray text-white">
            <div className="flex mb-4 text-xl bg-gray-800 rounded-full w-48">
                <button className="flex-1 py-2" onClick={() => { changeTime(15) }}>15</button>
                <button className="flex-1 py-2" onClick={() => { changeTime(30) }}>30</button>
                <button className="flex-1 py-2" onClick={() => { changeTime(60) }}>60</button>
                {/*<select className='border-none bg-transparent text-lg'>*/}
                {/*    <option value='engilish' className='bg-gray-800'>english</option>*/}
                {/*    <option value='russian' className='bg-gray-800'>russian</option>*/}
                {/*</select>*/}
            </div>
            <div className="text-2xl text-custom-yellow mb-4">{timeLeft}</div>
            <div className="relative w-full flex flex-col items-center">
                {!testCompleted ? (
                    <>
                        <div className="relative text-2xl">
                            {renderWords(wordsLine, inputWords)}
                        </div>
                        <div className="absolute w-full">
                            <input
                                className="w-full bg-transparent text-transparent border-none outline-none"
                                value={inputWords}
                                maxLength={words.length}
                                onChange={handleInput}
                                autoFocus
                            />
                        </div>
                    </>
                ) : (
                    <div className="mb-4 text-2xl">
                        WPM: {Math.round(finalRes)}
                        <div>
                            Accuracy: {Math.round(accuracy)}%
                        </div>
                    </div>
                )}
                <button className='absolute top-full mt-10' onClick={() => testReset(initialTime)}>
                    <RotateCcw/>
                </button>
            </div>
        </div>
    );
};

export default TypingPractice;