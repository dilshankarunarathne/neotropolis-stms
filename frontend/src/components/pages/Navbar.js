import React from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <section>
    <div>
      <h1>Navbar</h1>
      <Link to="/login">Login</Link>

    </div>
    </section>
  )
}

export default Navbar