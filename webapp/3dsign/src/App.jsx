import { useState, Suspense } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import Hand from '3dsign\src\riggedhand.bin'
import Model from './Riggedhand'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <canvas>
        <ambientLight intensity={1.5}/>
        <OrbitControls/>
        <Suspense fallback={null}>
          <Model>
            <Hand/>
          </Model>
          
        </Suspense>
      </canvas>
    </>
  )
}

export default App
