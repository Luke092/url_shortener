import './App.css'
import {createBrowserRouter, RouterProvider, useLoaderData} from "react-router-dom";

function App() {

    const urlLoader = async ({params}) => {
        try {
            const resp = await fetch(`${window.config.basePath}/api/url/${params.id}`);

            if (resp.status > 299) {
                return null;
            }

            const result = await resp.json();
            return result;
        } catch (ex) {
            console.log(ex);
            return null;
        }
    }

    const router = createBrowserRouter([
        {
            path: "/",
            element: <ShortenerForm/>
        },
        {
            path: "/:id",
            loader: urlLoader,
            element: <Redirect/>
        }
    ])

    return (
        <>
            <RouterProvider router={router}/>
        </>
    )
}

function ShortenerForm() {
    return (
        <div>
            <span>URL:</span>
            <input type="text"/>
            <button>Shorten URL</button>
        </div>
    )
}

function Redirect() {
    const urlObj = useLoaderData();

    if (urlObj === null) {
        window.location.href = "/";
        return;
    }

    window.location.href = urlObj.url;

    return <></>
}

export default App
