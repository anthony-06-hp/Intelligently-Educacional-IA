// === LOGIN MODULE ===
let currentStepIndex = 0;
const steps = document.querySelectorAll('.step'); // 🔧 Esto soluciona el error

// Función para obtener cookie CSRF (necesaria para Django)
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
function showStep(index) {
  steps.forEach((step, i) => {
    step.style.display = i === index ? 'block' : 'none';
  });
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

// Inicializar mostrando el primer paso

showStep(currentStepIndex);

;

// === UTILIDADES GLOBALES ===
const Utils = {
    // Función para obtener CSRF token de Django
    getCSRFToken() {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
        return csrfToken ? csrfToken.value : null;
    },
    async makeRequest(url, method = 'POST', data = {}) {
        const csrfToken = this.getCSRFToken();
        
        const config = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            }
        };

        if (method !== 'GET') {
            config.body = JSON.stringify(data);
        }

        try {
            const response = await fetch(url, config);
            return await response.json();
        } catch (error) {
            console.error('Request failed:', error);
            throw error;
        }
    },

    // Función para mostrar notificaciones toast
    showToast(message, type = 'success') {
        // Crear elemento toast
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <div class="toast-content">
                <span>${message}</span>
                <button class="toast-close">&times;</button>
            </div>
        `;

        // Agregar estilos si no existen
        if (!document.getElementById('toast-styles')) {
            const style = document.createElement('style');
            style.id = 'toast-styles';
            style.textContent = `
                .toast {
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    min-width: 300px;
                    padding: 15px;
                    border-radius: 10px;
                    color: white;
                    z-index: 10000;
                    animation: slideInRight 0.3s ease;
                }
                .toast-success { background: #28a745; }
                .toast-error { background: #dc3545; }
                .toast-warning { background: #ffc107; color: #333; }
                .toast-info { background: #17a2b8; }
                .toast-content {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .toast-close {
                    background: none;
                    border: none;
                    color: inherit;
                    font-size: 18px;
                    cursor: pointer;
                    padding: 0;
                    margin-left: 10px;
                }
                @keyframes slideInRight {
                    from { transform: translateX(100%); opacity: 0; }
                    to { transform: translateX(0); opacity: 1; }
                }
            `;
            document.head.appendChild(style);
        }

        // Agregar al DOM
        document.body.appendChild(toast);

        // Cerrar al hacer clic
        toast.querySelector('.toast-close').addEventListener('click', () => {
            toast.remove();
        });

        // Auto cerrar después de 5 segundos
        setTimeout(() => {
            if (toast.parentNode) {
                toast.remove();
            }
        }, 5000);
    }
};

// Exportar para uso global
// window.LoginModule = LoginModule;
window.Utils = Utils;

// === REGISTER PAGE FUNCTIONALITY ===
const totalSteps = 3;

function showTab(stepIndex) {
    // Hide all sections
    document.querySelectorAll('.form-section').forEach(section => {
        section.classList.remove('active');
    });
    
    // Remove active class from all tabs
    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Show selected section and tab
    const targetSection = document.getElementById(`step${stepIndex + 1}`);
    const targetTab = document.querySelectorAll('.tab')[stepIndex];
    
    if (targetSection) targetSection.classList.add('active');
    if (targetTab) targetTab.classList.add('active');
    
    currentStepIndex = stepIndex;
    updateStepIndicator();
    updateNavigationButtons();
}

function nextStep() {
    if (currentStepIndex < totalSteps - 1) {
        if (validateCurrentStep()) {
            showTab(currentStepIndex + 1);
        }
    }
}

function previousStep() {
    if (currentStepIndex > 0) {
        showTab(currentStepIndex - 1);
    }
}

function updateStepIndicator() {
    const stepElement = document.getElementById('currentStep');
    if (stepElement) {
        stepElement.textContent = currentStepIndex + 1;
    }
}

function updateNavigationButtons() {
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const registerBtn = document.getElementById('registerBtn');

    if (prevBtn) prevBtn.style.display = currentStepIndex === 0 ? 'none' : 'block';
    if (nextBtn) nextBtn.style.display = currentStepIndex === totalSteps - 1 ? 'none' : 'block';
    if (registerBtn) registerBtn.style.display = currentStepIndex === totalSteps - 1 ? 'block' : 'none';
}

function validateCurrentStep() {
    const currentSection = document.getElementById(`step${currentStepIndex + 1}`);
    if (!currentSection) return false;
    
    const requiredInputs = currentSection.querySelectorAll('input[required]');
    
    for (let input of requiredInputs) {
        if (!input.value.trim()) {
            const label = input.labels && input.labels[0] ? input.labels[0].textContent : 'This';
            Swal.fire({icon : 'error', title: 'Error', text: `${label} is required!`});
            input.classList.add('error');
            input.focus();
            return false;
        }
    }

    // Validate passwords match on first step
    if (currentStepIndex === 0) {
        const password = document.getElementById('password');
        const confirmPassword = document.getElementById('confirmPassword');
        
        if (password && confirmPassword && password.value !== confirmPassword.value) {
            Swal.fire({icon: 'error', title: 'Error', text: 'Passwords do not match!'});
            password.classList.add('error');
            return false;
        }
    }

    return true;
}

function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.getElementById('imagePreview');
            const uploadIcon = document.querySelector('.upload-icon');
            
            if (preview && uploadIcon) {
                preview.src = e.target.result;
                preview.style.display = 'block';
                uploadIcon.style.display = 'none';
            }
        };
        reader.readAsDataURL(file);
    }
}

function selectAvatar(element, emoji) {
    // Remove selected class from all avatars
    document.querySelectorAll('.avatar-option').forEach(option => {
        option.classList.remove('selected');
    });
    
    // Add selected class to clicked avatar
    element.classList.add('selected');
    
    // Update upload area with selected avatar
    const uploadIcon = document.querySelector('.upload-icon');
    const imagePreview = document.getElementById('imagePreview');
    
    if (uploadIcon && imagePreview) {
        uploadIcon.textContent = emoji;
        uploadIcon.style.display = 'block';
        imagePreview.style.display = 'none';
    }
    
    // Clear file input
    const fileInput = document.getElementById('fileInput');
    if (fileInput) fileInput.value = '';
}

// Initialize register page when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Only run on register page
    if (document.getElementById('registerForm')) {
        updateStepIndicator();
        updateNavigationButtons();
        
        // Form submission
        const registerForm = document.getElementById('registerForm');
        if (registerForm) {
            registerForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                if (validateCurrentStep()) {
                    // Let Django handle the form submission
                    this.submit();
                }
            });
        }
    }
});

// Dashboard JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    console.log('Dashboard cargado exitosamente');
    
    // Initialize dashboard components
    initializeSidebar();
    // initializeCourseCards();
    // initializeUserMenu();
    
    // // Check if user is authenticated (Django template will handle this)
    // // but we can add client-side enhancements
    // setupDashboardInteractions();
});

// Sidebar navigation functionality
function initializeSidebar() {
    const navItems = document.querySelectorAll('.nav-item:not(#logout-btn)');
    
    navItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all nav items
            navItems.forEach(nav => nav.classList.remove('active'));
            
            // Add active class to clicked item
            this.classList.add('active');
            
            // Get section name
            // const sectionName = this.querySelector('span:last-child').textContent.trim();
            // console.log('Navegando a:', sectionName);
            
            // Here you can add logic to load different sections
            // loadSection(sectionName);
            
            // Show loading state or navigate to different views
            // showLoadingState(sectionName);
        });
    });
document.addEventListener('DOMContentLoaded', () => {
  // Logout functionality
  const logoutBtn = document.getElementById('logout-btn');
  if (logoutBtn) {
      logoutBtn.addEventListener('click', handleLogout);
  }
});

// Handle logout
function handleLogout(e) {
  e.preventDefault();

  Swal.fire({
    title: '¿Cerrar sesión?',
    text: '¿Estás seguro de que quieres cerrar sesión?',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, cerrar sesión',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.isConfirmed) {
      const logoutForm = document.getElementById('logout-form');
      if (logoutForm) {
        logoutForm.submit();
      } else {
        window.location.href = '/accounts/logout/';
      }
    }
  });
}

// Course cards functionality
function initializeCourseCards() {
    // Course action buttons
    const modifyButtons = document.querySelectorAll('.btn-outline');
    const viewButtons = document.querySelectorAll('.btn-primary');
    const courseMenus = document.querySelectorAll('.course-menu');
    
    modifyButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Modificando curso...');
            showNotification('Función de modificar curso próximamente', 'info');
        });
    });
    
    viewButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Viendo clase...');
            showNotification('Cargando clase...', 'success');
            // Here you would navigate to the course view
        });
    });
    
    courseMenus.forEach(menu => {
        menu.addEventListener('click', function(e) {
            e.stopPropagation();
            console.log('Abriendo menú de curso...');
            showCourseContextMenu(this);
        });
    });
}

// User menu interactions
function initializeUserMenu() {
    const iniciarClaseBtn = document.querySelector('.iniciar-clase-btn');
    
    if (iniciarClaseBtn) {
        iniciarClaseBtn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Iniciando nueva clase...');
            showNotification('Iniciando nueva clase...', 'success');
            // Here you would open the create class modal or navigate to create class page
        });
    }
    
    // User avatar click (could open profile menu)
    const userAvatar = document.querySelector('.user-avatar');
    if (userAvatar) {
        userAvatar.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Abriendo menú de usuario...');
            // showUserMenu();
        });
    }
}

// Show loading state for navigation
// function showLoadingState(sectionName) {
//     // You can implement a loading overlay or skeleton screen here
//     console.log(`Cargando sección: ${sectionName}`);
    
//     // Example: temporarily disable navigation during "loading"
//     const navItems = document.querySelectorAll('.nav-item');
//     navItems.forEach(item => item.style.pointerEvents = 'none');
    
//     setTimeout(() => {
//         navItems.forEach(item => item.style.pointerEvents = 'auto');
//         console.log(`Sección ${sectionName} cargada`);
//     }, 500);
// }

// Show course context menu
function showCourseContextMenu(menuButton) {
    // Remove any existing context menus
    const existingMenu = document.querySelector('.course-context-menu');
    if (existingMenu) {
        existingMenu.remove();
    }
    
    // Create context menu
    const contextMenu = document.createElement('div');
    contextMenu.className = 'course-context-menu';
    contextMenu.innerHTML = `
        <div class="context-menu-item" onclick="editCourse()">Editar</div>
        <div class="context-menu-item" onclick="duplicateCourse()">Duplicar</div>
        <div class="context-menu-item" onclick="shareCourse()">Compartir</div>
        <hr>
        <div class="context-menu-item danger" onclick="deleteCourse()">Eliminar</div>
    `;
    
    // Position the menu
    const rect = menuButton.getBoundingClientRect();
    contextMenu.style.cssText = `
        position: fixed;
        top: ${rect.bottom + 5}px;
        left: ${rect.left - 100}px;
        background: white;
        border: 1px solid #e8e8ea;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        z-index: 1001;
        min-width: 120px;
        padding: 8px 0;
    `;
    
    // Add styles for menu items
    const style = document.createElement('style');
    style.textContent = `
        .context-menu-item {
            padding: 8px 16px;
            font-size: 12px;
            cursor: pointer;
            color: #1d1d1f;
        }
        .context-menu-item:hover {
            background: #f5f5f7;
        }
        .context-menu-item.danger {
            color: #ff3b30;
        }
        .context-menu-item.danger:hover {
            background: #ffebee;
        }
    `;
    
    document.head.appendChild(style);
    document.body.appendChild(contextMenu);
    
    // Close menu when clicking outside
    setTimeout(() => {
        document.addEventListener('click', function closeMenu(e) {
            if (!contextMenu.contains(e.target)) {
                contextMenu.remove();
                style.remove();
                document.removeEventListener('click', closeMenu);
            }
        });
    }, 100);
}

// Course context menu actions
function editCourse() {
    console.log('Editando curso...');
    showNotification('Abriendo editor de curso...', 'info');
}

function duplicateCourse() {
    console.log('Duplicando curso...');
    showNotification('Curso duplicado exitosamente', 'success');
}

function shareCourse() {
    console.log('Compartiendo curso...');
    showNotification('Enlace de compartir copiado', 'success');
}

function deleteCourse() {
    if (confirm('¿Estás seguro de que quieres eliminar este curso?')) {
        console.log('Eliminando curso...');
        showNotification('Curso eliminado', 'error');
    }
}

// Setup general dashboard interactions
function setupDashboardInteractions() {
    // Assignment cards
    const assignmentActions = document.querySelectorAll('.assignment-action');
    assignmentActions.forEach(action => {
        action.addEventListener('click', function(e) {
            e.preventDefault();
            const subject = this.closest('.assignment-card').querySelector('.assignment-subject').textContent;
            console.log(`Viendo asignatura: ${subject}`);
            showNotification(`Cargando ${subject}...`, 'info');
        });
    });
    
     // Add keyboard shortcuts
    setupKeyboardShortcuts();
    
    // Initialize mobile menu if needed
    setupMobileMenu();
}

// Keyboard shortcuts
function setupKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Alt + N: New class
        if (e.altKey && e.key === 'n') {
            e.preventDefault();
            document.querySelector('.iniciar-clase-btn')?.click();
        }
        
        // Alt + H: Go to Home
        if (e.altKey && e.key === 'h') {
            e.preventDefault();
            document.querySelector('.nav-item.active')?.click();
        }
        
        // Escape: Close any open menus
        if (e.key === 'Escape') {
            const contextMenu = document.querySelector('.course-context-menu');
            if (contextMenu) {
                contextMenu.remove();
            }
        }
    });
}

// Mobile menu setup
function setupMobileMenu() {
    // Create mobile menu toggle if it doesn't exist
    if (window.innerWidth <= 768 && !document.querySelector('.mobile-menu-toggle')) {
        createMobileMenuToggle();
    }
    
    // Handle window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            const sidebar = document.querySelector('.sidebar');
            sidebar.classList.remove('open');
        }
    });
}

// Create mobile menu toggle
function createMobileMenuToggle() {
    const toggle = document.createElement('button');
    toggle.className = 'mobile-menu-toggle';
    toggle.innerHTML = '☰';
    toggle.style.cssText = `
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 1002;
        background: white;
        border: 1px solid #e8e8ea;
        border-radius: 6px;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    `;
    
    toggle.addEventListener('click', function() {
        const sidebar = document.querySelector('.sidebar');
        sidebar.classList.toggle('open');
    });
    
    document.body.appendChild(toggle);
    
    // Hide toggle on desktop
    const mediaQuery = window.matchMedia('(min-width: 769px)');
    function handleMediaQuery(e) {
        toggle.style.display = e.matches ? 'none' : 'flex';
    }
    mediaQuery.addListener(handleMediaQuery);
    handleMediaQuery(mediaQuery);
}

// Notification system
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotification = document.querySelector('.dashboard-notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    const notification = document.createElement('div');
    notification.className = `dashboard-notification ${type}`;
    
    const colors = {
        success: '#34c759',
        error: '#ff3b30',
        info: '#007aff',
        warning: '#ff9500'
    };
    
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${colors[type] || colors.info};
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 500;
        z-index: 1003;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    
    notification.textContent = message;
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Loading states for buttons
function setButtonLoading(button, loading = true) {
    if (loading) {
        button.dataset.originalText = button.textContent;
        button.textContent = 'Cargando...';
        button.disabled = true;
        button.style.opacity = '0.7';
    } else {
        button.textContent = button.dataset.originalText || button.textContent;
        button.disabled = false;
        button.style.opacity = '1';
    }
}

// Progress circle animation (for the stats panel)
function animateProgressCircle() {
    const progressCircles = document.querySelectorAll('[class*="circle-progress-"]');
    
    progressCircles.forEach(circle => {
        const currentOffset = parseFloat(circle.style.strokeDashoffset || circle.getAttribute('stroke-dashoffset'));
        const circumference = 188.5; // 2 * π * r (r=30)
        
        // Animate from full circle to current position
        circle.style.strokeDashoffset = circumference;
        
        setTimeout(() => {
            circle.style.transition = 'stroke-dashoffset 1s ease-in-out';
            circle.style.strokeDashoffset = currentOffset;
        }, 500);
    });
}

// Initialize progress animation on load
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(animateProgressCircle, 1000);
});

// Utility functions for data handling
function formatDate(date) {
    const options = { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    return new Date(date).toLocaleDateString('es-ES', options);
}

function truncateText(text, maxLength = 100) {
    if (text.length <= maxLength) return text;
    return text.substring(0, maxLength) + '...';
}

// Search functionality (if needed)
function initializeSearch() {
    const searchInput = document.getElementById('dashboard-search');
    if (searchInput) {
        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                performSearch(this.value);
            }, 300);
        });
    }
}

function performSearch(query) {
    console.log('Buscando:', query);
    // Implement search logic here
    // You could filter courses, assignments, etc.
}

// Export functions for use in other scripts if needed
window.DashboardUtils = {
    showNotification,
    setButtonLoading,
    formatDate,
    truncateText
};
    }