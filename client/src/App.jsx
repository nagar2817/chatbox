import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [message, setMessage] = useState('')
  const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'

  useEffect(() => {
    axios.get(`${apiUrl}/api/hello`)
      .then(response => setMessage(response.data.message))
      .catch(error => console.error('Error:', error))
  }, [])

  return (
    <div>
      <h1>Message from backend: {message}</h1>
    </div>
  )
}

export default App