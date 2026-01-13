"use client"
import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
  const [sayHi, setContext] = useState("");

  useEffect(() => {
    axios.get("http://localhost:8000/api/data")
      .then(res => setContext(res.data.message))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
        <h1>{sayHi}</h1>
    </div>
  );
}
