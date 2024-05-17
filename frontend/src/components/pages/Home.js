import { useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import AuthContext from '../../context/AuthProvider';

function Home() {
  const { auth } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (!auth.user) {
      navigate('/login');
    }
  }, [auth, navigate]);

    return (
        <div>
            <h1>Welcome to Godai!</h1>
            <p>Unleashing AI for Rapid Prototyping and Streamlined Development</p>
        </div>
    );
}

export default Home;
