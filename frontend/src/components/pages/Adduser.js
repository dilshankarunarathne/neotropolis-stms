import React from 'react'


const Adduser = () => {
  return (
    <div id='adduser' className='adduser'>
       
    
        <form onSubmit={onSubmit} action="" className="adduser">
                <label htmlFor="">Your First Name</label>
                <input type="text"  name='name'/>

                <label htmlFor="">Your last Name</label>
                <input type="text"  name='name'/>


        </form>
         
    </div>
  )
}

export default Adduser