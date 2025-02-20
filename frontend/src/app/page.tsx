'use client'
import TypingTest from "@/components/TypingTest";
import {Source_Code_Pro} from "next/font/google"
import {User} from 'lucide-react'
import Link from 'next/link'

const source = Source_Code_Pro({subsets: ['latin']})

export default function Home() {

    return (
        <div>
            <div className='flex absolute right-0 p-12'>
                <Link href='/account' className='ml-auto'>
                    <User size={40}/>
                </Link>
            </div>
            <div className={source.className}>
                <TypingTest />
            </div>
        </div>
    )
}