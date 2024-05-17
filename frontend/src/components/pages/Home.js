import { useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import AuthContext from '../../context/AuthProvider';
import Navbar from '../Navbar';

function Home() {
  const { auth } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (!auth.user) {
      navigate('/login');
    }
  }, [auth, navigate]);

    return (
        <main>
           <Navbar />
            
        </main>
    );
}

export default Home;
