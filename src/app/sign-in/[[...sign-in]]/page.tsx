import { SignIn } from '@clerk/nextjs'
import React from 'react'

const page = () => {
  return (
    <div>
        <SignIn routing='hash'/>
    </div>
  )
}

export default page