
function MessageSender(text){
    this.BACKEND = "http://www.nkchatbot.com:8083";
    //this.BACKEND = "http://localhost:8000";
    this.QUESTION = text;
    this.ANSWER = "This is a default answer";
}

MessageSender.prototype.askChatbot = function(){
    let self = this;
    $.ajax({
        url: `${self.BACKEND}/ask/?question=${self.QUESTION}`,
        success:function(res){
            console.log(res);
            self.ANSWER = res.data.answer;
        },
        error:function(){self.ANSWER = "Sorry QA program fail!"}
    });
    return this;
};

MessageSender.prototype.getChatbotGreet = function(greetingType){
    let self = this;
    $.ajax({
        url: `${self.BACKEND}/greet/?mood=${greetingType}`,
        async:false,
    })
        .done(function (data) {
            console.log(data);
            self.ANSWER = data.data.greet;
        })
        .fail(function(){ self.ANSWER = "Sorry Greeting program fail!"});
    return this.ANSWER;
};

MessageSender.prototype.sendUserMessage = function () {
    let viewer = new MessageViewer(this.QUESTION);
    viewer.createChatMessage().addChatMessage();
    return this;
};

MessageSender.prototype.sendChatbotMessage = function () {
    let viewer = new MessageViewer(this.ANSWER, chatbot.CurrentMood);
    viewer.createChatMessage().addChatMessage();
    return this;
};

let initsender = new MessageSender();
initsender.getChatbotGreet('init');
initsender.sendChatbotMessage(chatbot.CurrentMood);
