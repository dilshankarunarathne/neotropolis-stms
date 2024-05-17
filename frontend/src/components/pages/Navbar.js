import React from 'react'
import './navbar.css';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <section>
      <h1>nav bar</h1>
        
        <Link to='/Navbar' >Login</Link>

        <Link to='/Login' >SignUp</Link>
    </section>
  )
}

export default Navbar