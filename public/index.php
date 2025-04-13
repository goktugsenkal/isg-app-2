<?php
// This file serves as the front controller, routing all incoming requests.
// Bu dosya, gelen tüm istekleri yönlendiren front controller görevi görür.

// Include Composer's autoloader to load all dependencies, including Dotenv.
// Tüm bağımlılıkları, Dotenv dahil, yüklemek için Composer'ın otomatik yükleyicisini dahil et.
require_once __DIR__ . '/../vendor/autoload.php';

use Dotenv\Dotenv;

// Load environment variables from the .env file located at the project root.
// Proje kök dizininde bulunan .env dosyasından ortam değişkenlerini yükle.
$dotenv = Dotenv::createImmutable(__DIR__ . '/../');
$dotenv->load();

// Retrieve the current request URI and extract just the path.
$requestUri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// Retrieve the current request URI and extract just the path.
// Mevcut istek URI'sini al ve sadece yol kısmını ayrıştır.
$baseUri = '/php_project_template/public';
$requestUri = str_replace($baseUri, '', $requestUri);

// Remove trailing slash for consistency (except for the root path).
// Tutarlılık için sondaki eğik çizgiyi kaldır (kök yol hariç).
if ($requestUri !== '/' && substr($requestUri, -1) === '/') {
    $requestUri = rtrim($requestUri, '/');
}

// Route the request based on the URI.
// URI'ye göre isteği yönlendir.
switch ($requestUri) {
    case '':
    case '/':
        // Home page
        require_once __DIR__ . '/../src/views/home.php';
        break;
    case '/isg':
        require_once __DIR__ . '/../src/views/isg.php';
        break;
    case '/about':
        require_once __DIR__ . '/../src/views/about.php';
        break;
    case '/portfolio':
        require_once __DIR__ . '/../src/views/portfolio.php';
        break;
    case '/services':
        require_once __DIR__ . '/../src/views/services.php';
        break;
    case '/contact':
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            require_once __DIR__ . '/../src/Controllers/ContactController.php';
        } else {
            require_once __DIR__ . '/../src/views/contact.php';
        }
        break;
    default:
        http_response_code(404);
        require_once __DIR__ . '/../src/views/404.php';
        break;
}