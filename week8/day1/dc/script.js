// Instructions
// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

// Create a class named Video. The class should be constructed with the following parameters:
// title (a string)
// uploader (a string, the person who uploaded it)
// time (a number, the duration of the video - in seconds)

class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }
    // Create a method called watch() which displays a string as follows:
    // “uploader parameter watched all time parameter of title parameter!”
    watch() {
        console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
    }

}


// Instantiate a new Video instance and call the watch() method.
const video1 = new Video("Funny Cats videos", "John", 180);
video1.watch();

// Instantiate a second Video instance with different values.
const video2 = new Video("JS Tutorial", "Alice", 300);
video2.watch();
// Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)

const videoData = [
    { title: "Music Video", uploader: "Sarah", time: 240 },
    { title: "Gaming Highlights", uploader: "Mike", time: 600 },
    { title: "Travel Vlog", uploader: "Emily", time: 420 },
    { title: "Tutorial Series", uploader: "David", time: 900 },
    { title: "Comedy Skit", uploader: "Olivia", time: 150 }
];
// Think of the best data structure to save this information within the array.
const videos = [];
for (const data of videoData) {
    const video = new Video(data.title, data.uploader, data.time);
    videos.push(video);
}
// Bonus: Loop through the array to instantiate those instances.
for (const video of videos) {
    video.watch();
}
