let currentStepIndex = 0;

const steps = document.querySelectorAll(".form-section");
const currentStepSpan = document.getElementById("currentStep");
const nextBtn = document.getElementById("nextBtn");
const prevBtn = document.getElementById("prevBtn");
const registerBtn = document.getElementById("registerBtn");

function showStep(index) {
    steps.forEach((step, i) => {
        step.classList.toggle("active", i === index);
    });

    currentStepSpan.textContent = index + 1;

    prevBtn.style.display = index === 0 ? "none" : "inline-block";
    nextBtn.style.display = index < steps.length - 1 ? "inline-block" : "none";
    registerBtn.style.display = index === steps.length - 1 ? "inline-block" : "none";
}

function nextStep() {
    if (currentStepIndex < steps.length - 1) {
        currentStepIndex++;
        showStep(currentStepIndex);
    }
}

function previousStep() {
    if (currentStepIndex > 0) {
        currentStepIndex--;
        showStep(currentStepIndex);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    showStep(currentStepIndex);
});
function selectAvatar(element, avatarEmoji) {
    document.getElementById('avatarInput').value = avatarEmoji;
    
    const allOptions = document.querySelectorAll('.avatar-option');
    allOptions.forEach(opt => opt.classList.remove('selected'));
    element.classList.add('selected');
}
