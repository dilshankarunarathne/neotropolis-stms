import React from 'react'
import './UpdateUser.css'

const UpdateUser = () => {
  return (
    <div id='UpdateUser' className='UpdateUser'>
    <form onSubmit={onSubmit} action="" className="UpdateUser">

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






  


export default UpdateUser