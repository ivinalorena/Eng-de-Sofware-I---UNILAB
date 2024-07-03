import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import { DefaultLayout } from '../layout'
import Home from '../pages/Home'


const router = createBrowserRouter([
    {
        path: '/',
        element: <DefaultLayout />,
        children: [
            {
                path: '/',
                element: <Home />
            },
        ],
    },


])

export function Routes() {
    return <RouterProvider router={router} />
}