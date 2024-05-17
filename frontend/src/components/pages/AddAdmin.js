import React from 'react'
import './AddAdmin.css'

const AddAdmin = () => {
  return (
    <div id='AddAdmin' className='AddAdmin'>
        <form onSubmit={onSubmit} action="" className="AddAdmin">

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

                <label htmlFor="">Admin Type</label>
                <input type="text" id='name' name='name'/>

                <label htmlFor="">Password</label>
                <input type="text" id='name' name='name'/>

                <label htmlFor="">Confirm your Password</label>
                <input type="text" id='name' name='name'/><br/>

                <label htmlFor="">Add Admin</label>
                <input type="text" id='name' name='name'/>




        </form>
         
    </div>
  )
}




export default AddAdmin