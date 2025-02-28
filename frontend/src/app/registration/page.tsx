'use client'

import { useRouter, useSearchParams } from "next/navigation"
import { useEffect, useState } from 'react'
import Account from "../account/page";
import { LockKeyholeIcon, UserRound } from "lucide-react";
import axios from "axios";
import {useSession} from 'next-auth/react'
import {useForm, SubmitHandler} from 'react-hook-form';
import { renderToStaticMarkup } from "react-dom/server";
import { toast } from 'react-hot-toast'

type Inputs = {
    username: string
    password: string
}

export default function Registration() {
    const {data: session} = useSession();
    const params = useSearchParams();
    const router = useRouter();
    const {
        register,
        handleSubmit,
        getValues,
        formState: {errors, isSubmitting},
    } = useForm<Inputs>({
        defaultValues: {
            username: '',
            password: '',
        },
    })

    useEffect(() => {
        if (session && session.user) {
            router.push('/');
        }
    }, [params, router, session])

    const formSubmit: SubmitHandler<Inputs> = async (form) => {
        const {username, password} = form

        try {
            const res = await axios.post('http://localhost:8000/api/users/registration', {
                username: username,
                password: password,
            });

            if (res.status === 200) {return router.push('/')
                
            } else {
                const data = await res.data;
                throw new Error(data.message);
              }
        } catch (err: any){
            const error = err.message && err.message.indexOf('E11000') === 0 ? 'username is duplicate' : err.message
            toast.error(error || 'error');
        }
    }

    return (
        <div className='flex h-screen bg-neutral-800'>
            <div className='flex-1 flex justify-center items-center'>
                <form className='bg-neutral-900 w-1/2 p-8 rounded-lg shadow-lg' onSubmit={handleSubmit(formSubmit)}>
                    <h2 className='text-center text-white opacity-70 text-2xl mb-6'><b>Registration</b></h2>
                    <div className='relative mb-4'>
                        <UserRound size={20} className='absolute left-2 top-1/2 -translate-y-1/2 text-white opacity-70'/>
                        <input 
                            className='bg-neutral-800 text-white p-2 pl-10 w-full rounded outline-none focus:ring-2 focus:ring-gray-600' 
                            type="text" 
                            {...register('username', {
                                required: 'Name is required',
                            })}
                        />
                    </div>
                    <div className='relative mb-4'>
                        <LockKeyholeIcon size={20} className='absolute left-2 top-1/2 -translate-y-1/2 text-white opacity-70'/>
                        <input 
                            className='bg-neutral-800 text-white p-2 pl-10 w-full rounded outline-none focus:ring-2 focus:ring-gray-600' 
                            type="password" 
                            {...register('password', {
                                required: 'password is required'
                            })}
                        />
                    </div>
                    <button 
                        className='bg-zinc-700 text-white p-2 w-full rounded hover:bg-zinc-600 transition-colors'
                        type="submit"
                        disabled={isSubmitting}
                    >
                        {isSubmitting && (
                            <span className="loading loading-spinner"></span>
                        )}
                        Registration
                    </button>
                </form>
            </div>
            <div className='flex-1'>
            </div>
        </div>
    )
}