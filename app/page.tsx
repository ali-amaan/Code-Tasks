import { ChatDemo } from "@/components/ui/chat-demo";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { ModeToggle } from "@/components/ui/mode-toggle";


export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <Card>
        <CardHeader>
          <div className="flex justify-around">
          <div>
          <CardTitle>Next Gen Chatbot</CardTitle>
          <CardDescription>AI Powered</CardDescription>
          </div>
          <div className="ml-auto"><ModeToggle /></div>
          </div>
          
        </CardHeader>
        <CardContent>
          <ChatDemo />
        </CardContent>
        <CardFooter>
          <p>Made with ❤️ at Nokia HQ Finland</p>
        </CardFooter>
      </Card>
    </main>
  );
}
