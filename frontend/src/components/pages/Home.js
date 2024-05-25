import { useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import AuthContext from '../../context/AuthProvider';
import { Link } from 'react-router-dom';

function Home() {
  const { auth } = useContext(AuthContext);
  const navigate = useNavigate();

    return (
        <div>
            <h1>Welcome to Godai!</h1>
            <p>Unleashing AI for Rapid Prototyping and Streamlined Development</p>
            <Link to='/About'>go to about page</Link>
        </div>
    );
}

export default Home;