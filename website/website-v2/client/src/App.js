import { createBrowserRouter, Outlet, RouterProvider } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import "./styles/App.scss";

const Layout = () => {
  return (
    <>
      <Sidebar />
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
