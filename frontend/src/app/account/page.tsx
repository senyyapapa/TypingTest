import { Undo2 } from 'lucide-react'
import Link from 'next/link'

export default function Account() {
    return (
        <div>
            <div>
                <Link href='/' className='flex absolute p-4 opacity-30'>
                    <Undo2 size={20} /> Back to main page
                </Link>
            </div>
        </div>
    )
}