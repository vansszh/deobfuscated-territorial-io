================================================================================
TERRITORIAL.IO - DEOBFUSCATED CODE DOCUMENTATION

File: index.html (Deobfuscated)
Backup: original_code.html (Original)
Total Lines: 34,124
Game Type: Browser-based multiplayer territory conquest game
Technologies: HTML5, JavaScript, Canvas API, WebSocket, Base64 encoding
Deobfuscation: ~96 batches of transformations applied

================================================================================
TABLE OF CONTENTS
================================================================================
1. CORE GAME SYSTEMS
2. USER INTERFACE COMPONENTS  
3. PLAYER & DATA MANAGEMENT
4. MAP & WORLD SYSTEMS
5. COMBAT & ATTACK SYSTEMS
6. AI & BOT SYSTEMS
7. NETWORKING & MULTIPLAYER
8. REPLAY SYSTEM
9. SETTINGS & CONFIGURATION
10. UTILITY & HELPER FUNCTIONS
11. RENDERING & GRAPHICS
12. INPUT HANDLING
13. CAMERA & VIEWPORT
14. COLOR SYSTEM
15. STORAGE & PERSISTENCE

================================================================================
DEOBFUSCATION SUMMARY
================================================================================

Key Renamed Classes/Constructors:
- GameState() - Main game state container
- GameLoop() - Game tick and frame management
- GameConfig() - Game configuration data
- MapManager() - Map rendering and management
- BotAIController() - Main bot AI system
- BotData() - Bot difficulty and behavior data
- TeamSystem() - Team assignments and colors
- NetworkController() - WebSocket communication
- RecentPlayersList() - Recently played with players
- LocalStorage() - Browser storage wrapper
- ColorConstants() - Color palette definitions
- CameraController() - Camera position and zoom
- Button() - UI button component
- Dialog() - Modal dialog component

Key Renamed Global Objects:
- gameConfig - Game configuration (was aD/c1)
- playerData - Player state data (was ag)
- worldTiles - Tile/map data (was ac)
- teamSystem - Team management (was bg)
- botAI - Bot AI controller (was bN)
- networkManager - Network handling (was b0)
- mapManager - Map system (was bS)
- replaySystem - Replay management (was b9)
- gameLoop - Main loop (was bf)
- settingsManager - Settings system
- attackManager - Attack handling
- statsTracker - Statistics tracking

================================================================================
1. CORE GAME SYSTEMS
================================================================================

GameState()
    - Main game state container
    - Properties:
      * totalPlayers - Total player count in game
      * humanPlayers - Number of human players
      * currentPlayerId - Local player's ID
      * isReplayMode - Whether watching replay
      * isSpectator - Spectator mode flag
      * isTeamGame - Team game mode flag
      * gameMode - Game mode (0-10)
      * isLocalGame - Local/offline game flag
      * botCount - Number of bots

GameLoop()
    - Main game loop controller
    - Properties:
      * needsRedraw - Flag to trigger canvas redraw
      * currentTime - Current game timestamp
      * tickInterval - Time between ticks (56ms)
    - Methods:
      * init() - Initialize game loop
      * update() - Main update tick
      * render() - Render frame

GameConfig()
    - Game configuration storage
    - Properties:
      * totalPlayers - Max players
      * maxDamage - Maximum damage per attack
      * mapWidth, mapHeight - Map dimensions
      * gameStarted, gameEnded, gamePaused - State flags
      * gameTime - Current game time
      * tickCount - Total ticks elapsed
      * frameCount - Frames rendered
      * deltaTime - Time since last frame
      * fps - Current framerate

================================================================================
2. USER INTERFACE COMPONENTS
================================================================================

Button()
    - Clickable button component
    - Methods:
      * init() - Initialize button
      * render() - Draw button
      * handleClick(x, y) - Check click hit

Dialog()
    - Modal dialog/popup window
    - Methods:
      * init() - Initialize dialog
      * render() - Draw dialog
      * open() - Show dialog
      * close() - Hide dialog

ContextMenu()
    - Right-click context menu
    - Player interaction options
    - Attack, ally, spectate options

NotificationSystem
    - Toast notifications
    - Methods:
      * showNotification() - Display message
      * showErrorMessage() - Error toast
      * showInfoMessage() - Info toast
      * hideNotification() - Remove toast

================================================================================
3. PLAYER & DATA MANAGEMENT
================================================================================

PlayerDataClass()
    - playerData object - Player state storage
    - Properties:
      * playerNames[] - Array of player names
      * playerStatus[] - 0=dead, 1=alive, 2=spectating
      * boundMinX[], boundMaxX[] - Territory bounds
      * boundMinY[], boundMaxY[] - Territory bounds
      * territoryCount[] - Tiles owned per player
      * balance[] - Resources/troops available
      * attackQueue[][] - Pending attacks per player
      * borderPixels[][] - Edge tiles (can attack from)
      * waterBorder[][] - Water edge tiles
      * interiorPixels[][] - Inner territory tiles

RecentPlayersList()
    - Manages recently played with players
    - Properties:
      * recentPlayersList[] - Array of player names
    - Methods:
      * init() - Load from storage
      * get() - Get list
      * getRecentPlayersData() - Get full data object
      * hasPlayer(playerName) - Check if in list
      * togglePlayer(playerName) - Add/remove from list
      * moveToTop(playerName) - Move to front of list
      * removeByIndex(index) - Remove by position
    - Internal:
      * addToRecentListInternal(playerName) - Add player
      * removeFromRecentListInternal(playerName) - Remove player

ActivePlayers()
    - Tracks currently active players
    - Methods:
      * update() - Refresh active list

================================================================================
4. MAP & WORLD SYSTEMS
================================================================================

MapManager()
    - mapManager object - Map rendering system
    - Properties:
      * mapWidth, mapHeight - Map dimensions
      * currentMode - Active map display mode
    - Methods:
      * init() - Initialize map
      * render() - Draw map to canvas
      * isMapMode(mode) - Check display mode

MapRenderer()
    - Handles map click interactions
    - Properties:
      * clickX, clickY - Last click position
    - Methods:
      * setClickPosition(x, y) - Store click coords
      * handleMapClick(code) - Process click (0=left, 1=right, 2=middle)
    - Internal:
      * handleLeftClickAction(tilePosition) - Left click handler
      * handleRightClickAction(tilePosition) - Right click handler
      * handleMiddleClickAction(tilePosition) - Middle click handler

World Tiles (worldTiles object):
    - Tile data and queries
    - Properties:
      * directionOffsets[] - [N, E, S, W] offsets
    - Methods:
      * isWater(tile) - Check if water tile
      * isLand(tile) - Check if land tile
      * isEmpty(tile) - Check if unowned
      * getOwner(tile) - Get owning player ID
      * setOwner(tile, player) - Set tile owner

Position Utilities (positionUtils):
    - Coordinate conversion
    - Methods:
      * createPos(x, y) - Create position value
      * screenToWorldX(screenX) - Convert screen to world
      * screenToWorldY(screenY) - Convert screen to world
      * isValidPosition(x, y) - Bounds check

================================================================================
5. COMBAT & ATTACK SYSTEMS
================================================================================

Attack Functions:
    cancelAttack()
        - Cancels current attack
        - Returns troops to attacker
        - Updates attack effects

    collectAttackTargets()
        - Gathers tiles to attack
        - Builds attack queue
        - Limits by maxTiles

    clearAttackQueue()
        - Empties attack queue for player
        - Resets water border tiles

    findTilesToAttack()
        - Locates valid attack targets
        - Calls findEnemyTiles() or findEmptyTiles()

    findEnemyTiles()
        - Finds adjacent enemy tiles
        - Uses direction offsets
        - Marks visited tiles

    findEmptyTiles()
        - Finds adjacent neutral tiles
        - For expanding into unclaimed territory

    applyTerritoryCapture()
        - Transfers tiles to attacker
        - Updates territory counts
        - Triggers team recalculation

    canCaptureTiles()
        - Checks if capture is possible
        - Routes to enemy or empty calculation

    calculateEnemyCapture()
        - Computes damage vs defense
        - Applies balance bonus
        - Returns capture success

    calculateEmptyCapture()
        - Simpler calculation for neutral tiles
        - No defense bonus

    applyDamageToAttacker(damageApplied, defenseBonus)
        - Reduces attacker resources
        - Applies defense bonus reduction
        - Records damage stats

    getAttackerDefenseBonus()
        - Gets defense bonus for attacker

    calculateBalanceBonus()
        - Computes bonus from balance/territory ratio

    addCapturedTilesToPlayer()
        - Adds captured tiles to player's territory
        - Updates border pixels
        - Sets tile ownership

    updateAttackerTerritory()
        - Refreshes attacker's territory data
        - Updates pixel lists
        - Applies team changes

Attack Manager (attackManager object):
    - Methods:
      * getAttackState(player) - Get attack status
      * clearAttack(player, index) - Remove attack
      * setAttackStrength(player, index, strength) - Set power
      * setAttackIndex(player, index) - Set attack index
      * setDefenseBonus(attacker, target, bonus) - Set bonus
      * getDefenseBonus(attacker, target) - Get bonus

Attack Effects (attackEffects object):
    - Methods:
      * showAttackEffect(player) - Visual feedback

Stats Tracker (statsTracker object):
    - Methods:
      * recordDamage(player, amount, type) - Log damage

Team Utilities (teamUtils object):
    - Methods:
      * startUpdate() - Begin territory update
      * updatePixelList(pixels) - Update pixel array
      * updateAttackQueue(queue) - Update attacks
      * clearPixelList(pixels) - Clear pixel array
      * finalizeUpdate() - Complete update
      * applyChanges() - Apply all changes
      * recalculateTerritory() - Full recalc

================================================================================
6. AI & BOT SYSTEMS
================================================================================

BotAIController()
    - botAI object - Main bot AI system
    - Sub-modules:
      * pathfinder - Position finding
      * decisionMaker - Strategy selection
      * attackTracker - Attack management

BotData()
    - Bot configuration and behavior
    - Properties:
      * botType[] - Difficulty per bot (0-6)
      * botNames[] - Difficulty level names
      * botDifficulty[] - Numeric difficulties
      * switchChance[] - Target switch probability
      * attackDelay[] - Time between attacks
      * neutralChance[] - Neutral attack probability
      * teamSizeBonus[] - Team bonus multipliers
      * defenseDelay[] - Defense timing
      * balanceTarget[] - Resource targets
    - Internal Variables:
      * botTimers[] - Action cooldowns
      * attackThreshold[] - Attack trigger levels
      * retreatThreshold[] - Retreat trigger levels
      * adaptRate[] - Learning speed
      * currentDelay[] - Current action delay
      * targetDelay[] - Target delay value
    - Methods:
      * init() - Initialize bot data
      * initLocale() - Load localized names
      * update(bot) - Update bot state

Bot Decision Functions:
    botTeamAttack(player, attackPower)
        - Team coordinated attack logic

    botCheckDefend(player)
        - Evaluate defensive needs

    botTeamSupport(player)
        - Support teammate logic

    botSoloAttack(player, attackPower)
        - Individual attack decision

    botExecuteAttack(player, attackPower, targetPlayerId, difficulty)
        - Execute chosen attack
        - Adjusts power based on target balance

    botAttackNeutral(player, attackPower)
        - Attack unclaimed territory

    botExpandTerritory(bot)
        - Territory expansion logic

    botFormAlliance(bot)
        - Alliance formation behavior

    botBreakAlliance(bot)
        - Alliance breaking behavior

Random Generator (randomGenerator object):
    - Methods:
      * shouldTrigger(chance) - Probability check
      * getInt(max) - Random integer
      * getRandom() - Random 0-1
      * getValue(max) - Random value

================================================================================
7. NETWORKING & MULTIPLAYER
================================================================================

NetworkController()
    - networkManager object
    - WebSocket communication
    - Methods:
      * connect() - Open connection
      * disconnect() - Close connection
      * send(data) - Send message
      * onMessage(handler) - Message callback

Leaderboard System (leaderboard object):
    - scoreboard sub-object:
      * isInTop(player) - Check if in top ranks
      * isEmpty() - Check if empty
      * getTarget(player) - Get attack target
      * getRandomTarget() - Random target
      * shouldSwitch() - Should change target
      * switchTarget() - Change target
      * getWeakTarget() - Find weak player
      * getNearbyTarget(player) - Find nearby target
      * setAttackTarget(player, target) - Set target
      * executeAttack(player, target, count, power) - Do attack
      * attackNeutral(player) - Attack empty tiles
    - teamStats sub-object:
      * setBalance(player, amount) - Set balance

================================================================================
8. REPLAY SYSTEM
================================================================================

ReplaySystem()
    - replaySystem object
    - Methods:
      * init() - Initialize replay
      * startRecording() - Begin capture
      * stopRecording() - End capture
      * saveReplay() - Export replay
      * loadReplay() - Import replay
      * playReplay() - Start playback
      * pauseReplay() - Pause playback
      * seekReplay(time) - Jump to time
      * getReplayTime() - Current position
      * getReplayDuration() - Total length

Replay Functions:
    processReplayTick()
        - Handle single replay tick

    applyReplayState()
        - Apply recorded state

    captureGameState()
        - Save current state

    restoreGameState()
        - Load saved state

    validateReplayData()
        - Check replay integrity

    encodeReplayFrame()
        - Compress frame data

    decodeReplayFrame()
        - Decompress frame data

    calculateReplayHash()
        - Generate replay checksum

================================================================================
9. SETTINGS & CONFIGURATION
================================================================================

SettingsManager()
    - settingsManager object
    - Properties:
      * settings.data[] - Array of setting values
    - Methods:
      * settings.save(index, value) - Save setting

Setting Functions:
    addNumberSetting(id, type, initial, default)
        - Register numeric setting

    addStringSetting(id, type, initial, default)
        - Register string setting

    expandSettingsArray(count)
        - Grow settings array

LocalStorage()
    - Platform storage wrapper
    - Methods:
      * getNumber(id, encrypted) - Get number
      * getString(id, encrypted) - Get string
      * getArray(length, encrypted) - Get array
      * save(id, value, encrypted) - Save value
      * saveArray(array, encrypted) - Save array
    - Platform Support:
      * platform.localStorage - Browser storage
      * platform.storageManager - Native storage
      * platform.memoryStorage - In-memory fallback
      * platform.storageWorker - Background worker

================================================================================
10. UTILITY & HELPER FUNCTIONS
================================================================================

Math Utilities (mathUtils object):
    - intDiv(a, b) - Integer division

Array Utilities (utils.array):
    - has(array, item) - Contains check

Player Utilities (utils.player):
    - getTroops(player, amount) - Get available troops
    - addTroops(player, amount) - Add troops
    - hasEnoughPlayers(type) - Player count check
    - isAlive(player) - Alive check

Color Utilities (utils.color):
    - rgb(r, g, b) - Create RGB color string
    - rgba(r, g, b, a) - Create RGBA color string

================================================================================
11. RENDERING & GRAPHICS
================================================================================

Sprite Renderer (spriteRenderer object):
    - Methods:
      * handleClick(x, y) - Click detection
    - Properties:
      * clickHandled - Click processed flag

Chat Manager (chatManager object):
    - Methods:
      * handleClick(x, y) - Click detection

Canvas Context (canvasContext):
    - 2D rendering context
    - Standard Canvas API methods

================================================================================
12. INPUT HANDLING
================================================================================

Input Functions:
    handleKeyDown(event)
        - Keyboard press handler

    handleKeyUp(event)
        - Keyboard release handler

    handleMouseMove(event)
        - Mouse movement handler

    handleMouseDown(event)
        - Mouse press handler

    handleMouseUp(event)
        - Mouse release handler

    handleTouchStart(event)
        - Touch begin handler

    handleTouchMove(event)
        - Touch drag handler

    handleTouchEnd(event)
        - Touch release handler

Keyboard Camera (keyboardCamera object):
    - Methods:
      * reset() - Reset camera controls

Action Handler (actionHandler object):
    - Methods:
      * applyZoom(ratio, offsetX, offsetY) - Apply zoom change

================================================================================
13. CAMERA & VIEWPORT
================================================================================

Camera Position (cameraPosition object):
    - Properties:
      * isLocked - Camera lock flag
    - Methods:
      * setX(x, offset) - Set X position
      * setY(y, offset) - Set Y position

Viewport Calculator (viewportCalc object):
    - Methods:
      * recalculate() - Update viewport bounds

Viewport Manager (viewportManager object):
    - Properties:
      * needsUpdate - Update flag

Camera Animation Variables:
    - targetCenterX, targetCenterY - Target position
    - targetZoom - Target zoom level
    - currentZoom - Current zoom level
    - isAnimating - Animation in progress
    - shouldLock - Lock after animation
    - animationProgress - 0 to 1 progress
    - animationSpeed - Current speed
    - baseAnimSpeed - Base animation speed
    - speedMultiplier - Speed modifier
    - animationDuration - Total duration
    - startCenterX, startCenterY - Start position
    - lastUpdateTime - Last update timestamp

Camera Methods:
    focusOnPlayer(player, speed, lock, zoom)
        - Center camera on player territory

    showFullMap(speed)
        - Show entire map

    setViewBounds(minX, minY, maxX, maxY)
        - Set camera bounds directly

    canMove()
        - Check if camera can be moved

    update()
        - Update camera animation

Internal Camera Functions:
    processHotkey(player)
        - Calculate center for player

    isHotkeyPressed(zoom, player)
        - Calculate zoom for player bounds

    clampZoomLevel(factor)
        - Prevent tiny zoom changes

    setViewBoundsInternal(minX, minY, maxX, maxY)
        - Internal bounds setting

    updateCameraAnimation()
        - Animate camera transition

================================================================================
14. COLOR SYSTEM
================================================================================

ColorConstants()
    - Predefined color palette
    - Uses colorUtils.rgb() and colorUtils.rgba()

Basic Colors:
    - black - RGB(0, 0, 0)
    - white - RGB(255, 255, 255)
    - gray - RGB(128, 128, 128)
    - lightGray - RGB(170, 170, 170)

Transparent Blacks:
    - blackTransparent70 - RGBA(0, 0, 0, 0.7)
    - blackTransparent50 - RGBA(0, 0, 0, 0.5)
    - blackTransparent85 - RGBA(0, 0, 0, 0.85)
    - blackTransparent60 - RGBA(0, 0, 0, 0.6)
    - blackTransparent35 - RGBA(0, 0, 0, 0.35)
    - darkBg - RGBA(0, 0, 0, 0.75)

Transparent Whites:
    - whiteTransparent30 - RGBA(255, 255, 255, 0.3)
    - whiteTransparent60 - RGBA(255, 255, 255, 0.6)
    - whiteTransparent25 - RGBA(255, 255, 255, 0.25)
    - whiteTransparent85 - RGBA(255, 255, 255, 0.85)
    - whiteTransparent75 - RGBA(255, 255, 255, 0.75)
    - whiteTransparent15 - RGBA(255, 255, 255, 0.15)
    - whiteTransparent11 - RGBA(255, 255, 255, 0.11)
    - lineColor - RGBA(255, 255, 255, 0.4)

UI Colors:
    - panelBg - RGBA(60, 60, 60, 0.85)
    - errorPanelBg - RGBA(80, 60, 60, 0.85)
    - darkGrayTransparent - RGBA(64, 64, 64, 0.75)
    - mediumGrayTransparent - RGBA(88, 88, 88, 0.83)
    - headerColor - RGBA(10, 60, 60, 0.9)

Green Variants:
    - positive - RGB(30, 255, 30)
    - neutral - RGB(0, 200, 0)
    - lightGreen - RGB(128, 255, 128)
    - brightGreen - RGB(0, 255, 0)
    - solidGreen - RGB(0, 120, 0)
    - paleGreen - RGB(190, 230, 190)
    - selectColor - RGBA(0, 200, 0, 0.5)
    - darkGreen - RGBA(0, 100, 0, 0.75)
    - darkerGreen - RGBA(0, 60, 0, 0.8)
    - veryDarkGreen - RGBA(0, 70, 0, 0.85)
    - greenBgDark - RGBA(10, 65, 10, 0.75)
    - greenTransparent60 - RGBA(0, 255, 0, 0.6)
    - greenTransparent50 - RGBA(0, 255, 0, 0.5)
    - greenTransparent30 - RGBA(0, 255, 0, 0.3)
    - greenHighlight - RGBA(0, 180, 0, 0.6)
    - greenDarkTransparent - RGBA(0, 120, 0, 0.85)

Red Variants:
    - lightRed - RGB(255, 120, 120)
    - statusGreen - RGB(255, 160, 160)
    - statusYellow - RGB(255, 70, 70)
    - statusRed - RGB(230, 0, 0)
    - orangeRed - RGB(255, 70, 10)
    - highlight - RGBA(255, 100, 100, 0.8)
    - darkRed - RGBA(100, 0, 0, 0.85)
    - darkerRed - RGBA(60, 0, 0, 0.85)
    - redTransparent60 - RGBA(220, 0, 0, 0.6)
    - redHighlight - RGBA(200, 0, 0, 0.6)
    - redDarkTransparent - RGBA(120, 0, 0, 0.85)

Blue Variants:
    - lightBlue - RGB(200, 235, 245)
    - infoColor - RGB(160, 160, 255)

================================================================================
15. STORAGE & PERSISTENCE
================================================================================

Platform Detection (platform object):
    - id: Platform type (0=browser, 1=native, 2=worker)
    - localStorage: Browser localStorage
    - storageManager: Native storage API
    - memoryStorage: In-memory object
    - storageWorker: Background worker

Storage Keys:
    - Prefix "d" + id: Default storage
    - Prefix "v" + id: Versioned storage
    - Prefix "e" + id: Encrypted storage
    - Prefix "l" + id: List storage

Settings Data Indices (partial):
    - [140]: Storage enabled flag
    - [161]: Recent players list (semicolon-separated)

================================================================================
GAME MODES
================================================================================

0 - Free For All
1 - Teams (Small)
2 - Teams (Large)
3 - Battle Royale
4 - Zombies
5 - 1v1
6 - Sandbox
7 - Custom
8 - Tournament
9 - Special Event

================================================================================
KEY MAPPINGS (Default)
================================================================================

Space - Center on player
Tab - Show leaderboard
Enter - Open chat
Escape - Close dialogs
1-9 - Quick select players
WASD/Arrows - Pan camera
+/- - Zoom in/out
M - Toggle minimap
P - Pause (local games)

================================================================================
WEBSOCKET PROTOCOL
================================================================================

Connection:
    - Connects to game server
    - Sends player authentication
    - Receives game state updates

Message Types:
    - Game state sync
    - Player actions
    - Attack commands
    - Chat messages
    - Team updates
    - Replay data

================================================================================
END OF DOCUMENTATION
================================================================================
