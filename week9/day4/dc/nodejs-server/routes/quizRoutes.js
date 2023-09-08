const express = require('express');
const router = express.Router();

const triviaQuestions = [
    {
        question: "What is the capital of France?",
        answer: "Paris",
    },
    {
        question: "Which planet is known as the Red Planet?",
        answer: "Mars",
    },
    {
        question: "What is the largest mammal in the world?",
        answer: "Blue whale",
    },
];

let currentQuestionIndex = 0;
let userScore = 0;

// Start the quiz and the first question
router.get('/', (req, res) => {
    if (currentQuestionIndex >= triviaQuestions.length) {
        res.json({ message: "Quiz completed! Your final score is: " + userScore });
    } else {
        // Display the current question
        const currentQuestion = triviaQuestions[currentQuestionIndex].question;
        res.json({ question: currentQuestion });
    }
});

// Submit an answer and move to the next question
router.post('/', (req, res) => {
    if (currentQuestionIndex >= triviaQuestions.length) {
        res.status(400).json({ error: "Quiz already completed" });
    } else {
        const userAnswer = req.body.answer;
        const correctAnswer = triviaQuestions[currentQuestionIndex].answer;

        if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
            // Correct answer
            userScore += 1;
            res.json({ message: "Correct! Your current score is: " + userScore });
        } else {
            // Incorrect answer
            res.json({ message: "Incorrect! Your current score is: " + userScore });
        }

        // Move to the next question
        currentQuestionIndex += 1;
    }
});

// final score of the quiz
router.get('/score', (req, res) => {
    res.json({ message: "Your final score is: " + userScore });
});

module.exports = router;
