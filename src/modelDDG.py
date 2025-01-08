# modelDDG.py
import asyncio
import json
from aiohttp import ClientSession, ClientTimeout

# API URLs
API_URL = "https://duckduckgo.com/duckchat/v1/chat"
VQD_URL = "https://duckduckgo.com/duckchat/v1/status"

# Function to get the vqd token
async def get_vqd(session: ClientSession) -> str:
    async with session.get(VQD_URL, headers={"x-vqd-accept": "1"}) as response:
        if response.status == 200:
            vqd = response.headers.get("x-vqd-4", "")
            if not vqd:
                raise Exception("Couldn't get the VQD token.")
            return vqd
        else:
            raise Exception(f"Error getting VQD: {response.status}")

# Function to send the messages and get the response
async def systemai(messages: list, model: str = "claude-3-haiku-20240307") -> str:
    async with ClientSession(timeout=ClientTimeout(total=30)) as session:
        # Get the VQD token
        vqd = await get_vqd(session)
        
        # Set headers
        headers = {
            "Content-Type": "application/json",
            "x-vqd-4": vqd,
        }
        
        # Prepare the data to send
        payload = {
            "model": model,
            "messages": messages,
        }

        try:
            async with session.post(API_URL, headers=headers, json=payload) as response:
                if response.content_type == 'text/event-stream':
                    complete_message = []  # To store the message chunks
                    async for line in response.content:
                        line = line.decode('utf-8').strip()
                        if line.startswith("data:"):
                            try:
                                message = json.loads(line[5:].strip())
                                if message.get("message"):
                                    complete_message.append(message["message"])  # Collect the message
                                if "DONE" in line:
                                    break
                            except json.JSONDecodeError:
                                continue  # Ignore errors in case of bad data
                    return "".join(complete_message) if complete_message else "No message received."
                else:
                    # If its a regular JSON response
                    result = await response.json()
                    return result.get("message", "No message received.")
        except Exception as e:
            return f"Error: {str(e)}"