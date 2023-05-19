import { createBrowserRouter, Outlet, RouterProvider } from "react-router-dom";
import Sidebar from "./components/Sidebar";

import Home from "./pages/Home";
import Uart from "./pages/UART";
import I2C from "./pages/I2C";

import Navbar from "./components/Navbar";
import "./styles/App.scss";
import Simulation from "./pages/Simulation";
import ContactUs from "./pages/ContactUs";

const Layout = () => {
  return (
    <>
      <Navbar />
      <div
        style={{
          display: "flex",
          alignContent: "space-between",
        }}
      >
        <Sidebar />
        <Outlet />
      </div>
    </>
  );
};

const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <div>
        <Layout />
      </div>
    ),
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/Uart",
        element: <Uart />,
      },
      {
        path: "/I2C",
        element: <I2C />,
      },
      {
        path: "/Uart",
        element: <Uart />,
      },
      {
        path: "/simulation",
        element: <Simulation />,
      },
      {
        path: "/contact-us",
        element: <ContactUs />,
      },
    ],
  },
  {},
]);

function App() {
  return (
    <div className="app">
      <div className="app_container">
        <RouterProvider router={router} />
      </div>
    </div>
  );
}

export default App;
