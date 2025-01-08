local HttpService = game:GetService("HttpService")

-- URL for the Python server running Flask
local url = "http://localhost:5000/gpt_response"  -- Make sure this URL is correct

-- Function to get a response from the server
local function response(user_input)
    -- Create the request data with the users message
    local requestData = {
        messages = user_input
    }

    -- Try to make the HTTP request with `pcall`
    local success, response = pcall(function()
        -- Convert the data into JSON
        local jsonData = HttpService:JSONEncode(requestData)
        
        -- Send the POST request to the given URL
        local response = HttpService:PostAsync(url, jsonData, Enum.HttpContentType.ApplicationJson)
        
        -- Return the response
        return response
    end)

    -- If the request was successful, process the response
    if success then
        local decodedResponse
        -- Try to decode the JSON response
        local successDecoding, decodedResponse = pcall(function()
            return HttpService:JSONDecode(response)
        end)

        if successDecoding then
            print("Response: " .. decodedResponse.response)
        else
            print("Error decoding the response: " .. decodedResponse)
        end
    else
        print("HTTP request error: " .. response)
    end
end

-- Call the function with a test message
response("Hello!")