import React, { useContext } from 'react';
import AuthContext from '../context/AuthProvider';
import './Navbar.css';

const Navbar = () => {
    const { auth, setAuth } = useContext(AuthContext);

    const handleLogout = () => {
        setAuth({});
        localStorage.removeItem('user');
    };

    return (
        <nav className="navbar">
            <div className="navbar-left">
                <h2>Neotropolis STMS</h2>
            </div>
            <div className="navbar-right">
                {auth.user ? (
                    <>
                        <span>Welcome, {auth.user}!</span>
                        <button onClick={handleLogout}>Logout</button>
                    </>
                ) : (
                    <>
                        <button>Sign In</button>
                        <button>Sign Up</button>
                    </>
                )}
            </div>
        </nav>
    );
};

export default Navbar;
