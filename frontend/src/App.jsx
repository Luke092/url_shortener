import './App.css'
import {createBrowserRouter, RouterProvider, useLoaderData} from "react-router-dom";
import {useEffect, useState} from "react";

function App() {

    const urlLoader = async ({params}) => {
        try {
            const resp = await fetch(`${window.config.basePath}/api/url/${params.id}`);

            if (resp.status > 299) {
                return null;
            }

            return await resp.json();
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
        <div className="layout">
            <RouterProvider router={router}/>
        </div>
    )
}

function ShortenerForm() {
    const [url, setUrl] = useState("");
    const [shorten, setShorten] = useState(null);
    const [toastVisible, setToastVisibility] = useState(false);

    const addUrl = async (url) => {
        if (!url || url === "") {
            setToastVisibility(true);
            return;
        }
        try {
            const resp = await fetch(`${window.config.basePath}/api/url/`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        url: url
                    })
                });

            if (resp.status > 299) {
                return null;
            }

            const result = await resp.json();
            setShorten(result.url_short)
        } catch (ex) {
            console.log(ex);
            return null;
        }
    }

    useEffect(() => {
        if (toastVisible) {
            const timeout = setTimeout(() => {
                setToastVisibility(false)
            }, 2000);
            return () => {
                clearTimeout(timeout);
            }
        }
    }, [toastVisible])

    if (shorten) {
        const completeUrlShort = `${window.location.protocol}//${window.location.host}/${shorten}`
        return (
            <>
                <div>
                    <h1
                        onClick={() => {
                            navigator.clipboard.writeText(completeUrlShort)
                                .then(() => {
                                    setToastVisibility(true);
                                })
                        }}
                    >
                        {completeUrlShort}
                    </h1>
                    <button
                        onClick={() => {
                            setShorten(null);
                            setUrl("")
                        }}>
                        Back
                    </button>
                </div>
                {toastVisible &&
                    <div className="toast__container">
                        <div className="toast">Url copied!</div>
                    </div>
                }</>
        )
    }

    return (
        <>
            <div className="shortener__container">
                <span>URL:</span>
                <input type="text"
                       value={url}
                       onChange={(e) => setUrl(e.target.value)}
                       onKeyUp={(e) => {
                           if (e.key === "Enter") {
                               addUrl(url);
                           }
                       }}
                />
                <button onClick={() => addUrl(url)}>Shorten URL</button>
            </div>
            {toastVisible &&
                <div className="toast__container">
                    <div className="toast toast--err">No url inserted!</div>
                </div>
            }
        </>
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
