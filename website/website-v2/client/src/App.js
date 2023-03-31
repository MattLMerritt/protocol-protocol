import { createBrowserRouter, Outlet, RouterProvider } from "react-router-dom";
import Sidebar from "./components/Sidebar";

import Home from "./pages/Home";

import Navbar from "./components/Navbar";
import "./styles/App.scss";

const Layout = () => {
  return (
    <div>
      <Navbar />
      <Sidebar />
      <Outlet />
    </div>
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
    ],
  },
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
