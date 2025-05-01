function getBotResponse(input) {
    if (input == "hi") {
        return "hello";
    } else if (input == "how are you") {
        return "Fine, thank you. How are you?";
    } else if (input == "fine") {
        return "Good, How Can We Help You?";
    } else if (input == "tell me about your services") {
        return "we are providing various facilities to our user like flight booking, hotel booking, tour guide hiring, vechile hiring and many more things";
    } else if (input == "do you provide special packages to your customer") {
        return "Yes, We are providing various package facilities to our customer";
    } else if (input == "where is your office located") {
        return "Koteshwor,Kathmandu,Nepal";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}
