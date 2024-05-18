"use client"
import Spline from "@splinetool/react-spline";
import Button from "../../components/Button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
export default function Home() {
  return (
    <main>
      <div>
      <Spline scene="https://prod.spline.design/yo-1h9es8G7RN0gz/scene.splinecode" />
      <h1 className="align-center absolute top-1/2  transform translate-x-1/2 -translate-y-1/2 text-[16rem] opacity-40">Cognito</h1>
      </div>
      <Dialog>
      <div className="flex justify-center items-center h-12">
        <DialogTrigger>
      <button>
      <Button 
      
      />
      </button>
      </DialogTrigger>
      <DialogContent>
    <DialogHeader>
      <DialogTitle className="text-black flex justify-center">Join Cognito</DialogTitle>
      <DialogDescription>
        
      </DialogDescription>
    </DialogHeader>
  </DialogContent>
      </div>
      </Dialog>
      
    </main>
    
  );
}
