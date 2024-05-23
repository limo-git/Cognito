import { notFound } from 'next/navigation'
import {FC} from 'react'
import { INFINITE_SCROLLING_PAGINATION_RESULTS } from '@/config'
import { PrismaClient } from '@prisma/client'
import Layout from './layout'

interface PageProps {
    params: {
        slug: string

    }

}
const prisma = new PrismaClient();
const Community = async ({params}: PageProps) => {
    const {slug} = params 
    const subreddit = await prisma.subreddit.findFirst({
        where: {name:slug},
        include:{
        posts:{
            include:{
                author:true,
                comments:true,
                subreddit:true,
            },
            take: INFINITE_SCROLLING_PAGINATION_RESULTS
        }
        }
    })
    if(!subreddit) return notFound()
    return <div className="flex justify-between mx-32 my-32 ">
        
    <div className="flex"><img alt="avatar"></img>
    <h1 className="font-bold text-3xl md:text-4xl h-14">Community name</h1></div>

    <div className="flex">
        <div>create post</div>
        <div>join</div>
    </div>

    </div>
}

export default Community