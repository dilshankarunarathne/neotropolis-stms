import React from 'react'
import './navbar.css';
import './Login'
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <section>
        <div className='signin'>
        <Link to='/login' >Sign In</Link>
        </div>

        <div className='signup'>
        <Link to='/login' >Sign Up</Link>
        </div>
    </section>
  )
}

export default Navbar