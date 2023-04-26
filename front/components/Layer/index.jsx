import React from 'react'
import Navbar from './Navbar'
export default function index({ children }) {
    return (
        <>
            <Navbar />
            <div>

                {children}
            </div>
        </>
    )
}
