import { useEffect, useState } from 'react'
import './App.css'

interface Task {
  id: string
  description: string
  done: boolean
}

// const fake_tasks: Task[] = [
// { id: '1231', description: 'Correr', done: false },
// { id: '131231', description: 'Comprar Roupa', done: false },
// { id: '3234', description: 'Estudar Renda Fixa', done: false },
// ]

function App() {

  // Estado
  const [tasks, setTasks] = useState<Task[]>([])

  useEffect(() => {
    async function loadTasks() {
      const url = 'http://localhost:8000/tasks/'
      const init = {
        method: 'GET',
        headers: {
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjAxSEJSVFI3WFRTVEdXWjZGTjY2RUhEVzdNIn0.tzfYgvOV41gpQJnH7k5OLnfN3y4h79i1HAvxL85XwRw'
        }
      }
      const response = await fetch(url, init)
      // alert(`status: ${response.status}`)

      if (response.status === 200) {
        const data = await response.json()
        // Atualiza o Estado
        setTasks(data)
      }
    }

    loadTasks()
  }, [])

  return (
    <>
      <header>
        <h1>Tasks - Web</h1>
      </header>
      <main>
        <h2>Tarefas cadastradas</h2>
        <ul>
          {tasks.map(task => <li>{task.description}</li>)}
        </ul>
      </main>
      <footer>
        <span>IFPI @ 2023</span>
      </footer>
    </>
  )
}

export default App
