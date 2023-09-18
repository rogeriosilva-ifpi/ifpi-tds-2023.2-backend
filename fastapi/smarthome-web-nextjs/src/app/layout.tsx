import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { Providers } from './providers'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'SmartHome - App',
  description: 'Sua casa inteligente!',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR" className='dark'>
      <body className="{inter.className} py-0 sm:py-4 box-border bg-zinc-700">
        <Providers>
          <div className='rounded-2xl shadow shadow-white flex flex-col p-4 mx-auto w-full h-screen sm:w-96 bg-primary'>
            <header className='h-20 flex justify-center items-center'>
              SmartHome App
            </header>
            {children}
            <footer className='h-10'>
              IFPI @ 2023
            </footer>
          </div>
        </Providers>
      </body>
    </html>
  )
}
