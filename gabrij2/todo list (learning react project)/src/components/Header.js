import PropTypes from 'prop-types'


const Header = ({ title }) => {
  return (
    <header>
        <h1> {title}</h1>
    </header>
  )
}

Header.defaultProps = {
    title: 'Task Tracker',
}

Header.PropTypes = {
    title: PropTypes.string
}

// //Css in JS
// const headingStyle = {
//     color:'red', 
//     backgroundColor: 'black'
// }

export default Header

// Class based

// import React from 'react'

// class App extends React.Component{
//     render() {
//         return <h1> Hello from a class</h1>
//     }
// }

// export default App