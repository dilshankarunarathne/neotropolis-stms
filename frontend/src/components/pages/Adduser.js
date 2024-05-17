import React from 'react'
import './Adduser.css'

const Adduser = () => {
  return (
    <div id='adduser' className='adduser'>
       
    
        <form onSubmit={onSubmit} action="" className="adduser">

                <label htmlFor="">first</label>
                <input type="text" id='name' name='name'/>

                <label htmlFor="">last</label>
                <input type="text" id='name' name='name'/><br/>

                <label htmlFor="">User Name</label>
                <input type="text" id='name' name='name'/>

                <label htmlFor="">Mobile Number</label>
                <input type="text" id='name' name='name'/><br/>

                <label htmlFor="">Email</label>
                <input type="text" id='name' name='name'/>

                <label htmlFor="">Password</label>
                <input type="text" id='name' name='name'/>

                <label htmlFor="">Confirm your Password</label>
                <input type="text" id='name' name='name'/><br/>

                <label htmlFor="">Add User</label>
                <input type="text" id='name' name='name'/>




        </form>
         
    </div>
  )
}

export default Adduser